import os

import pymysql
from dotenv import load_dotenv
from flask import Blueprint
from flask import jsonify

load_dotenv()

categories = Blueprint('categories', __name__)

config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'database': os.getenv('DB_NAME')
}


@categories.route('/api/v1/categories', methods=['GET'])
def category_list():
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    query = "select c.id as category_id, c.name as category_name, c.description as category_description FROM category c"

    cur.execute(query)
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()

    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))

    return jsonify(json_data)
