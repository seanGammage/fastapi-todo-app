# start.sh
#!/bin/bash

echo "Waiting for PostgreSQL to be ready..."
until pg_isready -h db -p 5432; do
  echo "Waiting for database..."
  sleep 2
done

echo "PostgreSQL is ready. Running migrations..."
uvicorn app.main:app --host 0.0.0.0 --port 8000
