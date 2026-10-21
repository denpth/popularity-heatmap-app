# Popularity Heat Map

An early prototype of a place-popularity heat map: a FastAPI backend reading visit counts from Postgres, a placeholder front end, and a small loader for a sample of visit data around Hampton Roads, Virginia. Personal side project, not coursework.

## Status

This is a skeleton, not a finished app. What works:

- `GET /health` on the API.
- `GET /now`, which returns the latest visit count per point of interest once the sample data is loaded.
- `pipeline/ingest_mobile_sample.py`, which loads `pipeline/sample/mobile_sample_hampton_roads.csv` into Postgres.

Not built yet: the React/Mapbox map (`frontend/src/Heatmap.tsx`, `ForecastCard.tsx` and `api.ts` are empty), the forecast in `backend/app/prediction.py` (returns an empty list), the Flink nowcast query, and the Terraform in `infra/`. `pipeline/ingest_safegraph.py` tries to download SafeGraph's free sample, which may no longer be available.

## Run it

```bash
cp .env.example .env        # set POSTGRES_PASSWORD; MAPBOX_TOKEN is for the planned map
docker compose up --build
docker compose exec api python pipeline/ingest_mobile_sample.py
```

Then open http://localhost:8000/health and http://localhost:8000/now.

## Layout

- `backend/`: FastAPI app and Dockerfile
- `frontend/`: placeholder page served by nginx, plus React/Vite stubs
- `pipeline/`: data loaders and the sample CSV
- `infra/`: Terraform stub
