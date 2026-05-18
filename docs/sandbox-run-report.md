# POSEIDON sandbox build & run report

Report date: 2026-05-18
Working directory used in the sandbox: `/tmp/poseidon-run/`
Host: macOS (Darwin 24), Java 17 (Temurin 17.0.2), Maven 3.x present, Gradle wrapper supplied by POSEIDON.

## 1. Use case

Validate that the POSEIDON-side of the building-block stack ends in something that actually runs. The nine `poseidon-input-*` bblocks plus the new `poseidon-output` target only have value if a real POSEIDON binary can consume a scenario that was produced from them. The goal of this sandbox experiment was to:

1. Build the upstream Java implementation of POSEIDON from source.
2. Run any scenario end-to-end.
3. Capture the native output and inspect its shape so the raw → EDITO transform documented in `_sources/poseidon-input-observation-output/description.md` can be implemented against a known artefact.

Out of scope (deferred): translating the JSON snippets in `_sources/poseidon-input-*/examples/*.json` into a unified runnable YAML. Started but not completed — see §7.

## 2. Approach

The approach was deliberately the smallest credible end-to-end loop:

1. Confirm JVM + Maven availability locally.
2. Clone POSEIDON shallow (`git clone --depth 1`) into `/tmp/poseidon-run/POSEIDON`.
3. Discover the build system (Gradle Kotlin DSL with a wrapper) and identify the main entry point (`uk.ac.ox.oxfish.YamlMain`).
4. Build a fat JAR via the Shadow plugin task: `:POSEIDON:shadowJar`. Skip tests and SpotBugs to keep the first iteration fast.
5. Pick the simplest bundled scenario (`POSEIDON/inputs/tests/replicate.yaml`) and run it through `YamlMain`.
6. On parse failure ("Component factory not found: …"), inspect the YAML loader (`uk.ac.ox.oxfish.utility.yaml.YamlConstructor`) and the supplier base class (`uk.ac.ox.poseidon.common.core.BasicFactorySupplier`) to understand how the factory-name registry is built.
7. Enumerate the *authoritative* factory-name list by running a small Java program that loads `FactorySupplier` via `ServiceLoader` against the built JAR (the same mechanism POSEIDON uses internally).
8. Diff the legacy YAML against the authoritative list, patch only the names that no longer resolve, re-run.
9. Inspect `output/pilot/result.yaml` to confirm the model produced metrics.

Why a clean enumeration of factory names instead of bisecting renames one by one: the bundled YAML samples in `inputs/YAML Samples/` and `inputs/tests/` predate a refactor that introduced explicit factory-name overrides per supplier. Some supplier classes still carry their pre-refactor display name (e.g. `Diffusing Logistic`, `Random Catchability`), others use the auto-derived name (`No discarding`, `Fish until full`). The only reliable source of truth is the runtime registry.

## 3. Test data

Two YAML files:

- **Starting point**: `/tmp/poseidon-run/POSEIDON/POSEIDON/inputs/tests/replicate.yaml` — a 50×50 km synthetic single-species fishery with 5 fishers, single port, MPA-Only regulation, fixed-price market, constant weather. This is the simplest scenario shipped in the repository.
- **Working scenario**: `/tmp/poseidon-run/scenarios/pilot.yaml` — `replicate.yaml` upscaled to 20 fishers on a 25×25 cell grid, with three factory names patched to current registry entries.

Patches applied (only these three):

| Field | Legacy value | Current registry name | Reason |
|---|---|---|---|
| `discardingStrategy` | `No Discarding` | `No discarding` | `BasicFactorySupplier.makeFactoryName` lowercases all CamelCase words after the first; `NoDiscardingFactorySupplier` has no override. |
| `fishingStrategy` | `Until Full With Day Limit` | `Fish until full` | Strategy class no longer present in the registry; nearest surviving equivalent. |
| `networkBuilder` | (n/a in `replicate.yaml`; would have been needed) | `Equal Out Degree` | Confirmed via the dumped registry. |

Run-time arguments:

- `--years 3` — three simulated years
- `--seed 42` — deterministic seed

No external data files were needed; the scenario is self-contained.

## 4. Execution

Concrete command sequence in chronological order (each line independent):

```bash
# 1. Tooling check
java -version          # OpenJDK 17.0.2 Temurin
which mvn              # /opt/homebrew/bin/mvn

# 2. Clone POSEIDON
mkdir -p /tmp/poseidon-run && cd /tmp/poseidon-run
git clone --depth 1 https://github.com/poseidon-fisheries/POSEIDON.git

# 3. Build the fat JAR (≈45 s on first cold build; Gradle 8.8 downloaded on first use)
cd /tmp/poseidon-run/POSEIDON
./gradlew :POSEIDON:shadowJar -x test -x spotbugsMain -x spotbugsTest --no-daemon

# Result: /tmp/poseidon-run/POSEIDON/POSEIDON/build/libs/POSEIDON-all.jar

# 4. Dump authoritative factory names (one-time discovery step)
cat > /tmp/poseidon-run/DumpFactories.java <<'EOF'
import java.util.ServiceLoader;
import uk.ac.ox.poseidon.common.api.FactorySupplier;
public class DumpFactories {
  public static void main(String[] a) {
    ServiceLoader.load(FactorySupplier.class)
        .forEach(s -> System.out.println(s.getFactoryName()));
  }
}
EOF
cd /tmp/poseidon-run
javac -cp POSEIDON/POSEIDON/build/libs/POSEIDON-all.jar DumpFactories.java
java -cp .:POSEIDON/POSEIDON/build/libs/POSEIDON-all.jar DumpFactories \
  | sort > factory_names.txt
# 387 lines — the canonical registry for this build.

# 5. Run the scenario
cd /tmp/poseidon-run
java -cp POSEIDON/POSEIDON/build/libs/POSEIDON-all.jar \
     uk.ac.ox.oxfish.YamlMain scenarios/pilot.yaml --years 3 --seed 42
```

Total wall-clock time for the working run: a few seconds. Build dominates first time (~45 s). Subsequent runs reuse the JAR.

## 5. Output

POSEIDON writes outputs to `./output/<scenarioBaseName>/` relative to the working directory. For the pilot run:

```
output/pilot/
├── result.yaml      180 KB   yearly aggregated metrics
├── scenario.yaml      2.5 KB the resolved scenario actually used
└── seed.txt           2 B    "42"
```

`result.yaml` top-level keys: `Fisher`, `FishState`, `FishState Daily`.

Sample yearly aggregate metrics (Year 0 / 1 / 2 across 20 fishers):

| Metric | Year 0 (mean) | Year 1 (mean) | Year 2 (mean) |
|---|---:|---:|---:|
| Species 0 Catches (kg) | 5 962 | 3 568 | 5 595 |
| Species 0 Landings (kg) | 5 495 | 3 310 | 5 195 |
| Earnings | 54 950 | 33 100 | 51 950 |
| Net cash flow | 54 031 | 32 220 | 50 890 |
| Variable costs | 919 | 880 | 1 060 |
| Hours of effort | 6 582 | 7 468 | 6 702 |
| Number of trips | 55 | 33 | 52 |
| Trip profits per hour | 15.40 | 4.02 | 7.37 |
| Mean trip duration (h) | 108 | 1 472 | 425 |
| Distance tow→port (km) | 64.7 | 52.1 | 60.1 |
| Active FADs | 0 | 0 | 0 |

Each metric is reported as `{Min, Max, Average, Count}` per simulated year. Mapping this raw structure to the `poseidon-output` target schema:

- `Fisher.<metric>.<year>` → `timeSeries[]` with `dimension: per-fisher`, written as one GeoParquet per metric, partitioned by year.
- `FishState.<metric>.<year>` → `timeSeries[]` with `dimension: global`.
- `FishState Daily.<metric>` → `timeSeries[]` with `cadence: daily`, partitioned by year.

The exact projection is the transformation table in `_sources/poseidon-input-observation-output/description.md`; this run produced a concrete artefact against which that table can now be tested.

## 6. Manual replication

Prerequisites: macOS or Linux, Java 17+, internet for the first build (Gradle wrapper + Maven Central deps), ~1.5 GB free disk.

Step by step:

1. **Clone POSEIDON** (≈30 s, ~600 MB checkout):
   ```bash
   mkdir -p /tmp/poseidon-run && cd /tmp/poseidon-run
   git clone --depth 1 https://github.com/poseidon-fisheries/POSEIDON.git
   ```

2. **Build the fat JAR** (≈45 s on a fresh machine; subsequent builds are seconds because Gradle caches):
   ```bash
   cd /tmp/poseidon-run/POSEIDON
   ./gradlew :POSEIDON:shadowJar -x test -x spotbugsMain -x spotbugsTest --no-daemon
   ```
   Look for `BUILD SUCCESSFUL` and confirm `POSEIDON/POSEIDON/build/libs/POSEIDON-all.jar` exists.

3. **(Optional, recommended) dump the factory registry** so you know which factory names are valid for this build:
   ```bash
   cd /tmp/poseidon-run
   cat > DumpFactories.java <<'EOF'
   import java.util.ServiceLoader;
   import uk.ac.ox.poseidon.common.api.FactorySupplier;
   public class DumpFactories {
     public static void main(String[] a) {
       ServiceLoader.load(FactorySupplier.class)
           .forEach(s -> System.out.println(s.getFactoryName()));
     }
   }
   EOF
   javac -cp POSEIDON/POSEIDON/build/libs/POSEIDON-all.jar DumpFactories.java
   java -cp .:POSEIDON/POSEIDON/build/libs/POSEIDON-all.jar DumpFactories \
     | sort > factory_names.txt
   ```
   This produces 387 lines on the current main branch. Use it to look up any "Component factory not found" error.

4. **Write the scenario YAML**. Create `/tmp/poseidon-run/scenarios/pilot.yaml` with the content shown in [Appendix A](#appendix-a--pilotyaml-used-in-this-run). Every factory name used MUST appear verbatim in `factory_names.txt`.

5. **Run**:
   ```bash
   cd /tmp/poseidon-run
   java -cp POSEIDON/POSEIDON/build/libs/POSEIDON-all.jar \
        uk.ac.ox.oxfish.YamlMain scenarios/pilot.yaml --years 3 --seed 42
   ```

6. **Inspect output**:
   ```bash
   cat output/pilot/seed.txt
   head -40 output/pilot/result.yaml
   python3 - <<'EOF'
   import yaml
   r = yaml.safe_load(open("output/pilot/result.yaml"))
   print("Top-level keys:", list(r.keys()))
   print("Fisher metrics:", list(r["Fisher"].keys())[:10])
   EOF
   ```

### Troubleshooting

- **`Cannot create property=X for JavaBean=…PrototypeScenario`** followed by `Component factory not found: <name>` — the factory name in YAML does not match any registered supplier. Look up the closest match in `factory_names.txt`. Note that capitalisation matters: `No Discarding` ≠ `No discarding`.
- **`./gradlew: Permission denied`** — `chmod +x ./gradlew` then retry. On a fresh git clone this is usually already executable.
- **OOM during build** — `export GRADLE_OPTS="-Xmx4g"` then retry. The default `gradle.properties` is generous but a constrained sandbox may need a hint.
- **Run does not print progress** — POSEIDON's `YamlMain` is quiet by default. Use `--log FINE` or `--log ALL` for verbose output.
- **`output/` directory missing** — `YamlMain` resolves it relative to the *current working directory*, not the JAR location. Always `cd` to a known directory before launching.

### Cleanup

```bash
rm -rf /tmp/poseidon-run
```

This wipes the build (and any further runs); it does not touch the repository content under `/Users/piotr/repos/seadots/bblocks-seadots/`.

## 7. What is *not* covered yet

The "inject bblock example inputs and re-run" step was started but not completed. The blockers are not technical — they are semantic:

- The JSON snippets under `_sources/poseidon-input-*/examples/*.json` describe the *bblock view* of each input, not POSEIDON's *native YAML* shape. Each snippet maps to a sub-tree of a POSEIDON scenario via a translation rule that lives in the Stage B description of the relevant bblock.
- To run them end-to-end we need a small translator (≤ 200 lines of Python or Java) that, given the set of bblock JSON examples and a scenario-axes choice (see `poseidon-input-scenario`), emits one POSEIDON YAML. The translator is itself worth a building-block — call it `poseidon-input-bundler` — but that is a separate piece of work.

A reasonable next step: implement that translator for the three smallest bblocks (biology / fleet / map) and re-run with their JSON examples as inputs. The factory-name registry produced in §4 step 4 is the lookup table the translator needs.

## Appendix A — `pilot.yaml` used in this run

```yaml
Abstract:
  biologyInitializer:
    Diffusing Logistic:
      carryingCapacity: '5000.0'
      differentialPercentageToMove: '0.001'
      percentageLimitOnDailyMovement: '0.01'
      grower:
          Independent Logistic Grower:
              steepness: '0.7'
  departingStrategy:
    Fixed Rest:
      hoursBetweenEachDeparture: '12.0'
  destinationStrategy:
    Imitator-Explorator:
      alwaysCopyBest: true
      dropInUtilityNeededForUnfriend: '-1.0'
      ignoreEdgeDirection: true
      probability:
        Adaptive Probability:
          explorationProbability: '0.8'
          explorationProbabilityMinimum: '0.01'
          imitationProbability: '1.0'
          incrementMultiplier: '0.02'
      stepSize: uniform 1.0 10.0
  enginePower: normal 100.0 10.0
  fishers: 20
  fishingStrategy: Fish until full
  fuelTankSize: '100000.0'
  gasPricePerLiter: '0.01'
  gear:
    Random Catchability:
      meanCatchabilityFirstSpecies: '0.01'
      meanCatchabilityOtherSpecies: '0.01'
      standardDeviationCatchabilityFirstSpecies: '0.0'
      standardDeviationCatchabilityOtherSpecies: '0.0'
      gasPerHourFished: '5.0'
  gearStrategy: Never Change Gear
  habitatInitializer: All Sand
  holdSize: '100.0'
  literPerKilometer: '10.0'
  mapInitializer:
    Simple Map:
      cellSizeInKilometers: '10.0'
      coastalRoughness: '4.0'
      depthSmoothing: '1000000.0'
      height: '25.0'
      width: '25.0'
  mapMakerDedicatedRandomSeed: 123
  market:
    Fixed Price Market:
      marketPrice: '10.0'
  networkBuilder:
    Equal Out Degree:
      degree: 2
  portPositionX: -1
  portPositionY: -1
  ports: 1
  regulation: MPA Only
  speedInKmh: '5.0'
  startingMPAs: []
  usePredictors: false
  weatherInitializer:
    Constant Weather:
      temperature: '15.0'
      windOrientation: '0.0'
      windSpeed: '0.0'
  weatherStrategy: Ignore Weather
  discardingStrategy: No discarding
  cheaters: false
```

## Appendix B — outcome summary

| Step | Outcome |
|---|---|
| Clone | OK (≈30 s, 5490 files) |
| Build (`:POSEIDON:shadowJar`) | OK (BUILD SUCCESSFUL in 45 s) |
| First run attempt — `Abstract.yaml` | Failed: legacy factory names not in current registry |
| Factory-registry dump | OK (387 names) |
| Second run — patched `pilot.yaml` | OK; produced `output/pilot/{result.yaml, scenario.yaml, seed.txt}` |
| Output → EDITO transform | Not run here; concrete `result.yaml` is now available as the input fixture for that pipeline (see `_sources/poseidon-input-observation-output/description.md`) |
