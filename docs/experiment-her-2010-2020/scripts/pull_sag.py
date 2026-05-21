"""Pull ICES SAG SSB time-series for her.27.25-2932 (Central Baltic herring),
2023 single-stock advice, assessment key 17816.

Source endpoints (open, no auth):
  - getListStocks       -> resolves assessmentKey for stock + year
  - getStockDownloadData -> full-precision per-year time series
  - getFishStockReferencePoints

Provenance (all values below are TRACEABLE to a real source):
  - Time series:  ICES SAG getStockDownloadData, assessmentKey=17816
  - Report DOI:   embedded in the API response (10.17895/ices.advice.21820506.v1)
  - MSY Btrigger in tonnes: ICES Advice 2023, sh.her.27.25-2932 PDF
                  ( https://doi.org/10.17895/ices.advice.21820506.v1 ), value
                  1,034,000 t. The API only returns the ratio (MSY-Btrigger=1).
"""
import csv
import requests
import xml.etree.ElementTree as ET

URL = "https://standardgraphs.ices.dk/StandardGraphsWebServices.asmx/getStockDownloadData?assessmentKey=17816"
NS = "{http://standardgraphs.ices.dk/}"
MSY_BTRIGGER_TONNES = 1_034_000   # source: ICES advice DOI above (PDF table)

r = requests.get(URL, timeout=30)
r.raise_for_status()
root = ET.fromstring(r.text)

rows = []
for e in root:
    d = {c.tag.split('}')[-1]: (c.text or '').strip() for c in e}
    try:
        year = int(d.get("Year") or 0)
    except Exception:
        continue
    if not year:
        continue
    def num(v):
        try:
            return float(v)
        except Exception:
            return None
    ssb_ratio = num(d.get("StockSize"))
    rows.append({
        "year": year,
        "ssb_ratio": ssb_ratio,
        "low_ssb_ratio": num(d.get("Low_StockSize")),
        "high_ssb_ratio": num(d.get("High_StockSize")),
        "recruitment_thousands": num(d.get("Recruitment")),
        "F_ratio": num(d.get("FishingPressure")),
        "catches_t": num(d.get("Catches")),
        "ssb_t": ssb_ratio * MSY_BTRIGGER_TONNES if ssb_ratio is not None else None,
    })

target = [r for r in rows if 2010 <= r["year"] <= 2020]
print(f"Pulled {len(rows)} years; pilot window 2010-2020 has {len(target)} years")
for r in target:
    print(f'  {r["year"]}: SSB={r["ssb_t"]:,.0f} t  (ratio {r["ssb_ratio"]:.3f})  F/Fmsy={r["F_ratio"]:.3f}  catches={r["catches_t"]:,.0f} t')

OUT = "/tmp/poseidon-run/experiments/her-2010-2020/data/sag_her27_2532.csv"
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["year","ssb_ratio","ssb_t","low_ssb_ratio","high_ssb_ratio","recruitment_thousands","F_ratio","catches_t"])
    w.writeheader()
    w.writerows(rows)
print(f"\nWrote {OUT}")
