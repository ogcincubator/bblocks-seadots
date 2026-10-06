#!/usr/bin/env python3
"""Offline-friendly validation of the protected-area building blocks.

Does for the blocks under the given roots what the bblocks-postprocess CI does, without Docker:

  1. JSON Schema validation of every JSON / GeoJSON example snippet against its block's schema.
     `bblocks://<id>` references resolve to this repository's _sources for local blocks and to the
     annotated schemas of the imported registers (bblocks-config.yaml `imports`, followed
     transitively) for everything else. Remote documents are cached under ~/.cache/bblocks-validate.
  2. JSON-LD uplift of every example with the contexts of the block and of everything it depends on.
  3. SHACL validation of the uplifted graphs with the rules.shacl of all blocks under the roots;
     every declared ontology (bblock.json `ontology`) must parse as Turtle.
  4. Every transform in transforms.yaml is run the way postprocess runs it (the script is exec'd
     with `input_data` and `transform_metadata` in its globals and must set `output_data`) on the
     block's snippets whose language matches the transform's input media type; each output is
     validated against the transform's output profiles.
  5. The shell contract tests in <block>/transform-tests/*.sh are run.

Usage (from the repository root):
    python tools/validate_protected_areas.py [_sources/emodnet-protected-area _sources/protected-area]
Requires: jsonschema, referencing, pyld, rdflib, pyshacl, pyyaml, requests (and jq for the shell tests).
"""
import copy, hashlib, json, os, re, subprocess, sys, types
from pathlib import Path

import requests
import yaml
from jsonschema import Draft202012Validator
from jsonschema.exceptions import best_match
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012
from pyld import jsonld
import rdflib
from pyshacl import validate as shacl_validate

REPO = Path(__file__).resolve().parent.parent
SOURCES = REPO / "_sources"
CACHE = Path.home() / ".cache" / "bblocks-validate"
META_REGISTER = "https://w3id.org/ogc/bblocks/meta-register.json"
DEFAULT_REGISTER = "https://opengeospatial.github.io/bblocks/register.json"
MEDIA_TYPES = {"json": "application/json", "geojson": "application/geo+json", "jsonld": "application/ld+json"}


def fetch(url):
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / hashlib.sha1(url.encode()).hexdigest()
    if not f.exists():
        r = requests.get(url, timeout=60, headers={"Accept": "application/json, application/yaml, */*"})
        r.raise_for_status()
        f.write_bytes(r.content)
    return f.read_text(encoding="utf-8")


def load(path_or_url):
    s = str(path_or_url)
    text = fetch(s) if s.startswith("http") else Path(s).read_text(encoding="utf-8")
    return yaml.safe_load(text) if s.endswith((".yaml", ".yml")) else json.loads(text)


class Register:
    """Local blocks under _sources plus the imported registers, keyed by bblock id."""

    def __init__(self):
        cfg = yaml.safe_load((REPO / "bblocks-config.yaml").read_text(encoding="utf-8"))
        self.prefix = cfg["identifier-prefix"]
        self.local = {}                                    # id -> block dir
        for bj in SOURCES.glob("**/bblock.json"):
            rel = bj.parent.relative_to(SOURCES)
            self.local[self.prefix + ".".join(rel.parts)] = bj.parent
        self.remote = {}                                   # id -> register entry
        aliases = None
        todo, seen = list(cfg.get("imports", [])), set()
        while todo:
            imp = todo.pop()
            if imp == "default":
                imp = DEFAULT_REGISTER
            elif imp.startswith("@"):
                if aliases is None:
                    aliases = self._aliases()
                imp = aliases[imp]
            if imp in seen:
                continue
            seen.add(imp)
            reg = load(imp)
            for b in reg["bblocks"] if isinstance(reg, dict) else reg:
                self.remote.setdefault(b["itemIdentifier"], b)
            todo.extend(reg.get("imports", []) if isinstance(reg, dict) else [])

    @staticmethod
    def _aliases():
        """The meta-register is a flat map of `@org/register` aliases to register.json URLs."""
        return requests.get(META_REGISTER, timeout=60).json()

    def meta(self, bid):
        if bid in self.local:
            return json.loads((self.local[bid] / "bblock.json").read_text(encoding="utf-8"))
        return self.remote[bid]

    def schema_location(self, bid):
        if bid in self.local:
            return str(next(p for n in ("schema.yaml", "schema.json") if (p := self.local[bid] / n).exists()))
        s = self.remote[bid].get("schema", {})
        return s.get("application/yaml") or s.get("application/json")

    def context(self, bid):
        if bid in self.local:
            m = self.meta(bid)
            p = self.local[bid] / m.get("ldContext", "context.jsonld")
            return load(p)["@context"] if p.exists() else None
        url = self.remote.get(bid, {}).get("ldContext")
        return url

    def dependencies(self, bid, seen=None):
        """bid's dependsOn closure, dependencies first."""
        seen = set() if seen is None else seen
        out = []
        deps = list(self.meta(bid).get("dependsOn", []))
        if bid in self.local:                      # postprocess also follows the schema's bblocks:// refs
            deps += re.findall(r"bblocks://([\w.\-]+)", Path(self.schema_location(bid)).read_text(encoding="utf-8"))
        for dep in dict.fromkeys(deps):
            dep = dep.replace("bblocks://", "")
            if dep == bid:
                continue
            if dep not in seen and (dep in self.local or dep in self.remote):
                seen.add(dep)
                out += self.dependencies(dep, seen) + [dep]
        return out


def main(roots):
    reg = Register()
    roots = [Path(r).resolve() for r in roots]
    ours = {bid: d for bid, d in reg.local.items() if any(d == r or r in d.parents for r in roots)}

    def retrieve(uri):
        if uri.startswith("bblocks://"):
            loc = reg.schema_location(uri[len("bblocks://"):].split("#")[0])
        else:
            loc = uri.split("#")[0]
        return Resource.from_contents(load(loc), default_specification=DRAFT202012)

    registry = Registry(retrieve=retrieve)

    def validator(bid):
        schema = load(reg.schema_location(bid))
        schema.setdefault("$id", "bblocks://" + bid)
        return Draft202012Validator(schema, registry=registry)

    def loader(url, options=None):
        return {"contextUrl": None, "documentUrl": url, "document": json.loads(fetch(url))}
    jsonld.set_document_loader(loader)

    def context_chain(bid):
        return [c for d in reg.dependencies(bid) + [bid] if (c := reg.context(d))]

    def shape_sources(bid):
        """SHACL files of bid and of everything it depends on, as postprocess applies them."""
        out = []
        for b in reg.dependencies(bid) + [bid]:
            if b in reg.local:
                out += [str(reg.local[b] / f) for f in reg.meta(b).get("shaclRules", [])]
            else:
                for urls in (reg.remote[b].get("shaclShapes") or {}).values():
                    out += urls
        return list(dict.fromkeys(out))

    shape_graphs = {}

    def shapes_for(bid):
        g = rdflib.Graph()
        for src in shape_sources(bid):
            if src not in shape_graphs:
                shape_graphs[src] = rdflib.Graph().parse(data=fetch(src) if src.startswith("http")
                                                         else Path(src).read_text(encoding="utf-8"), format="turtle")
            g += shape_graphs[src]
        return g
    failures = 0
    for bid, d in sorted(ours.items()):
        onto = reg.meta(bid).get("ontology")
        if onto and not onto.startswith("http"):
            g = rdflib.Graph().parse(d / onto, format="turtle")
            print(f"ontology {bid}: {onto} parses, {len(g)} triples")

    def check(bid, doc, label):
        nonlocal failures
        errs = sorted(validator(bid).iter_errors(doc), key=lambda e: list(e.path))
        if errs:
            failures += 1
            for e in errs[:5]:
                e = best_match([e])                     # descend into oneOf/anyOf to the specific cause
                while e.context:
                    e = best_match(e.context)
                print(f"  FAIL {label} [{'/'.join(map(str, e.absolute_path))}] {e.message[:300]}")
            return
        chain = context_chain(bid)
        if not chain or doc.get("type") not in ("Feature", "FeatureCollection"):
            print(f"  ok   {label} (schema)")
            return
        docs = doc["features"] if doc.get("type") == "FeatureCollection" else [doc]
        ld = {"@context": chain, "@graph": copy.deepcopy(docs)}
        for f in ld["@graph"]:
            if f.get("id") is not None and ":" not in str(f["id"]):
                f["id"] = f"https://example.org/feature/{f['id']}"
        g = rdflib.Graph().parse(data=jsonld.to_rdf(ld, {"format": "application/n-quads"}), format="nquads")
        conforms, _, text = shacl_validate(g, shacl_graph=shapes_for(bid), inference="none")
        if not conforms:
            failures += 1
            print(f"  SHACL FAIL {label}\n{text[:1500]}")
            return
        else:
            print(f"  ok   {label}: schema, {len(g)} triples, SHACL ({len(shape_sources(bid))} shape files)")

    for bid, d in sorted(ours.items()):
        ex = d / "examples.yaml"
        snippets = []
        if ex.exists():
            for e in yaml.safe_load(ex.read_text(encoding="utf-8")).get("examples", []):
                snippets += [s for s in e.get("snippets", []) if s.get("language") in MEDIA_TYPES]
        if snippets:
            print(bid)
        for s in snippets:
            check(bid, load(d / s["ref"]), s["ref"])

        tf = d / "transforms.yaml"
        if not tf.exists():
            continue
        for t in yaml.safe_load(tf.read_text(encoding="utf-8"))["transforms"]:
            if t["type"] != "python":
                continue
            code = compile((d / t["ref"]).read_text(encoding="utf-8"), str(d / t["ref"]), "exec")
            for s in snippets:
                if MEDIA_TYPES[s["language"]] not in t["inputs"]["mediaTypes"]:
                    continue
                tm = types.SimpleNamespace(
                    metadata=types.SimpleNamespace(**t.get("metadata", {}), get=t.get("metadata", {}).get),
                    context=types.SimpleNamespace(bblock_id=bid, bblock_files_path=os.path.relpath(d, REPO)))
                ns = {"input_data": (d / s["ref"]).read_text(encoding="utf-8"), "output_data": None,
                      "transform_metadata": tm}
                cwd = os.getcwd()
                os.chdir(REPO)
                try:
                    exec(code, ns)
                finally:
                    os.chdir(cwd)
                out = json.loads(ns["output_data"])
                for prof in t["outputs"].get("profiles", []):
                    check(prof.replace("bblocks://", ""), out, f"{t['id']}({s['ref']}) -> {prof.rsplit('.', 1)[-1]}")
                if (rep := out.get("seadotsTransformReport")) is not None:
                    check(reg.prefix + "protected-area.transform-report", rep, f"{t['id']}({s['ref']}) report")

        for sh in sorted(d.glob("transform-tests/*.sh")):
            r = subprocess.run(["sh", str(sh)], capture_output=True, text=True)
            print(f"  {'ok  ' if r.returncode == 0 else 'FAIL'} {sh.relative_to(REPO)} {r.stderr.strip()[:300]}")
            failures += r.returncode != 0

    print("RESULT:", "all checks passed" if not failures else f"{failures} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or [str(SOURCES / "emodnet-protected-area"), str(SOURCES / "protected-area")]))
