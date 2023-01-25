FROM python:3.11

WORKDIR /code

ENV DB_PORT 3306

COPY requirements.txt .

RUN MARIADB_CONFIG=/usr/bin/mariadb_config pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:80", "api:app"]
