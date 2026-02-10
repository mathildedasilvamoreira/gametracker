FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    bash \
    default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x scripts/*.sh || true

# CETTE LIGNE EST LA CLÉ : elle garde le conteneur en vie
CMD ["bash", "scripts/run_pipeline.sh"]