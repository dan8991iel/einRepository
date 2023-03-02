FROM python:3.11

WORKDIR /code

ENV DB_PORT 3306
ENV GOOGLE_APPLICATION_CREDENTIALS firebase_service_account.json

COPY requirements.txt .

RUN pip install --upgrade -r /code/requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:80", "api:app"]
