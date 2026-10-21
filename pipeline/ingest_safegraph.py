"""
 Robust SafeGraph sample loader.
 • Tries the official free URL first
 • Falls back to a GitHub-hosted mirror if that fails
 • Writes the response to /tmp for inspection when unexpected
"""
import os, io, zipfile, requests, pandas as pd
from sqlalchemy import create_engine

DEST = "/tmp/safegraph_patterns.zip"
PRIMARY = "https://safegraph-data.s3.amazonaws.com/free/csv/2023/01/core_poi-geometry-patterns.zip"
FALLBACK = "https://github.com/achillesrasquinha/awesome-safegraph/raw/master/datasets/core_poi-geometry-patterns-2023-01.zip"

engine = create_engine(os.getenv("DATABASE_URL"))
def fetch(url):
    print(f"Downloading {url} …")
    r = requests.get(url, timeout=60, headers={"User-Agent": "Mozilla/5.0"}, allow_redirects=True)
    if r.status_code != 200 or r.headers.get("content-type", "").startswith("text/html"):
        print(f"→ Got {r.status_code} / {r.headers.get('content-type')} — not a zip.")
        return None
    with open(DEST, "wb") as f:
        f.write(r.content)
    return DEST

path = fetch(PRIMARY) or fetch(FALLBACK)
if not path:
    raise RuntimeError("Could not download SafeGraph sample.")

with zipfile.ZipFile(path) as z:
    csv_name = [n for n in z.namelist() if n.endswith(".csv")][0]
    df = pd.read_csv(z.open(csv_name))

subset = df[["placekey","location_name","latitude","longitude",
             "date_range_start","raw_visit_counts"]]
subset.to_sql("patterns", engine, if_exists="replace", index=False)
print("Loaded", len(subset), "rows into Postgres.")
