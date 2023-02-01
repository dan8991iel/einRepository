FROM python:3.11

WORKDIR /code

ENV DB_PORT 3306

RUN apt-get update && apt-get install -y gcc wget
RUN wget https://dlm.mariadb.com/2678574/Connectors/c/connector-c-3.3.3/mariadb-connector-c-3.3.3-debian-bullseye-amd64.tar.gz -O - | tar -zxf - --strip-components=1 -C /usr
RUN pip install --upgrade pip

COPY requirements.txt .

RUN MARIADB_CONFIG=/usr/bin/mariadb_config pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:80", "api:app"]
