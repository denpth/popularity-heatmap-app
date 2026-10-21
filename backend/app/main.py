
from fastapi import FastAPI
from sqlalchemy import text
from database import engine

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/now")
def now():
    sql = text("""
        SELECT poi_id, name, lat, lon, visits
        FROM poi_visits
        WHERE timestamp_utc = (SELECT max(timestamp_utc) FROM poi_visits)
    """)
    rows = [dict(r) for r in engine.execute(sql)]
    return rows
