FROM python:3.13-slim-bookworm

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# Fuerza la versión segura de setuptools al final
RUN pip install --no-cache-dir setuptools==78.1.1

COPY . .

EXPOSE 5000

CMD ["python", "run.py"]
