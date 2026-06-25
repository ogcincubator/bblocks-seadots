import { create } from 'zustand';
import type { Concept, Term, Triple } from '../rdf/model';
import { tripleKey } from '../rdf/model';
import {
  fetchConceptList,
  fetchConcept,
  fetchSchemes,
  fetchTermIndex,
  fetchPredicates,
  update as sparqlUpdate,
  type ConceptListItem,
  type SchemeItem,
} from '../sparql/client';
import { toSparqlUpdate, toTurtle } from '../rdf/serialize';
import { config } from '../config';

/**
 * Pending edits are tracked as two triple sets relative to what is currently in
 * the store: `added` triples to insert, `removed` triples to delete. A locally
 * created concept simply shows up as a bundle of `added` triples whose subject
 * is not yet in the remote graph.
 */
interface StoreState {
  // Catalog ---------------------------------------------------------------
  conceptList: ConceptListItem[];
  schemes: SchemeItem[];
  terms: Term[];
  predicates: string[];
  loading: boolean;
  loadError: string | null;
  loadCatalog: () => Promise<void>;

  // Single concept cache --------------------------------------------------
  conceptCache: Record<string, Concept>;
  loadConcept: (iri: string) => Promise<Concept>;

  // Pending edits ---------------------------------------------------------
  added: Triple[];
  removed: Triple[];
  addTriple: (t: Triple) => void;
  removeTriple: (t: Triple) => void;
  /** Triples currently in effect for a subject (remote + added − removed). */
  effectiveTriples: (iri: string) => Triple[];
  discardChanges: () => void;

  // Persistence -----------------------------------------------------------
  pushToSparql: () => Promise<void>;
  /** Commit the pending additions to git via the backend API. */
  commitToGit: (message: string, filename?: string) => Promise<GitCommitResult>;
}

export interface GitCommitResult {
  commit: string;
  branch: string;
  file: string;
  pushed: boolean;
}

function keyset(ts: Triple[]): Set<string> {
  return new Set(ts.map(tripleKey));
}

export const useStore = create<StoreState>((set, get) => ({
  conceptList: [],
  schemes: [],
  terms: [],
  predicates: [],
  loading: false,
  loadError: null,

  async loadCatalog() {
    set({ loading: true, loadError: null });
    try {
      const [conceptList, schemes, terms, predicates] = await Promise.all([
        fetchConceptList(),
        fetchSchemes(),
        fetchTermIndex(),
        fetchPredicates(),
      ]);
      set({ conceptList, schemes, terms, predicates, loading: false });
    } catch (e) {
      set({ loading: false, loadError: (e as Error).message });
    }
  },

  conceptCache: {},
  async loadConcept(iri) {
    const cached = get().conceptCache[iri];
    if (cached) return cached;
    const concept = await fetchConcept(iri);
    set((s) => ({ conceptCache: { ...s.conceptCache, [iri]: concept } }));
    return concept;
  },

  added: [],
  removed: [],

  addTriple(t) {
    set((s) => {
      // If this exact triple was queued for removal, just cancel that.
      const remKeys = keyset(s.removed);
      if (remKeys.has(tripleKey(t))) {
        return { removed: s.removed.filter((x) => tripleKey(x) !== tripleKey(t)) };
      }
      if (keyset(s.added).has(tripleKey(t))) return {}; // already added
      return { added: [...s.added, t] };
    });
  },

  removeTriple(t) {
    set((s) => {
      // If it was a pending addition, drop it from `added` instead.
      if (keyset(s.added).has(tripleKey(t))) {
        return { added: s.added.filter((x) => tripleKey(x) !== tripleKey(t)) };
      }
      if (keyset(s.removed).has(tripleKey(t))) return {};
      return { removed: [...s.removed, t] };
    });
  },

  effectiveTriples(iri) {
    const s = get();
    const remote = s.conceptCache[iri]?.triples ?? [];
    const remKeys = keyset(s.removed);
    const base = remote.filter((t) => !remKeys.has(tripleKey(t)));
    const baseKeys = keyset(base);
    const adds = s.added.filter(
      (t) => t.subject === iri && !baseKeys.has(tripleKey(t)),
    );
    return [...base, ...adds];
  },

  discardChanges() {
    set({ added: [], removed: [] });
  },

  async pushToSparql() {
    const { added, removed } = get();
    if (!added.length && !removed.length) return;
    await sparqlUpdate(toSparqlUpdate(added, removed));
    // Invalidate caches so a re-open reflects the server state.
    set({ added: [], removed: [], conceptCache: {} });
    await get().loadCatalog();
  },

  async commitToGit(message, filename) {
    const { added } = get();
    if (!added.length) throw new Error('No additions to commit.');
    const res = await fetch(`${config.apiBase}/api/git/commit`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ turtle: toTurtle(added), message, filename }),
    });
    const json = await res.json().catch(() => ({}));
    if (!res.ok || !json.ok) {
      throw new Error(json.error || `Git commit failed (${res.status})`);
    }
    return json as GitCommitResult;
  },
}));
