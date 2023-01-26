FROM python:3.7-slim

WORKDIR /app

COPY api_yamdb/requirements.txt

RUN apt-get update && apt-get -y install libpq-dev gcc

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY api_yamdb/ /app

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]