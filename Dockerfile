FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Install PostgreSQL client tools for pg_isready
RUN apt-get update && apt-get install -y postgresql-client

COPY . .

CMD ["bash", "/app/scripts/start.sh"]
