"""
Load the sample Hampton Roads mobile-device visits into Postgres.
Run once inside the api container:

docker compose exec api python pipeline/ingest_mobile_sample.py

(DATABASE_URL is already set in the api container by docker-compose.yml.)
"""
import os, pandas as pd
from sqlalchemy import create_engine

FILE = "pipeline/sample/mobile_sample_hampton_roads.csv"
engine = create_engine(os.getenv("DATABASE_URL"))

df = pd.read_csv(FILE, parse_dates=["timestamp_utc"])
df.to_sql("poi_visits", engine, if_exists="replace", index=False)
print("Loaded", len(df), "rows into poi_visits.")
