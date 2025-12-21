FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    chromium \
    chromium-driver \
    libzbar0 \
    tzdata \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copiando os arquivos do codigo fonte
COPY perso_messages.json .
COPY relationships.json .
COPY src src/
COPY main.py .

CMD ["python", "main.py"]
