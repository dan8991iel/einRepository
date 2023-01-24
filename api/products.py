import mariadb
import sys
import os
import simplejson as json
from dotenv import load_dotenv
from flask import request, jsonify
from flask import Blueprint

load_dotenv()

products = Blueprint('products', __name__)

config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT')),
    'database': os.getenv('DB_NAME')
}


@products.route('/api/v1/products', methods=['GET'])
def product_list():
    conn = mariadb.connect(**config)
    cur = conn.cursor()

    query = "select p.id, p.name, p.price, p.description, p.image_url, c.name as cat_name FROM product p LEFT JOIN " \
            "category c " \
            "ON p.category_id = c.id"

    cur.execute(query)
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()

    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))

    return jsonify(json_data)
