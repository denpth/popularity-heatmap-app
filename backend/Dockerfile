FROM python:3.12-slim
WORKDIR /app

RUN pip install fastapi uvicorn pandas sqlalchemy requests psycopg2-binary

# copy FastAPI code
COPY backend/app ./app
# copy the whole pipeline folder so exec can find it
COPY pipeline ./pipeline


EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
