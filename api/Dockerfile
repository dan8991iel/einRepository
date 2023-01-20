FROM tiangolo/uwsgi-nginx-flask:python3.11

ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static

WORKDIR /var/www

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .