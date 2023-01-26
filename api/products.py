import os
import pymysql
from dotenv import load_dotenv
from flask import Blueprint
from flask import request, jsonify

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
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    query = "select p.id, p.name, p.price, p.description, p.image_url, c.name as category_name FROM product p LEFT JOIN " \
            "category c " \
            "ON p.category_id = c.id"

    cur.execute(query)
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()

    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))

    return jsonify(json_data)


@products.route('/api/v1/products', methods=['POST'])
def add_product():
    product_to_add = request.get_json(force=True)

    if product_to_add['name'] == '':
        return "Name missing!", 400
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    check_category_query = "select id from category c where name = %s"
    cur.execute(check_category_query, (product_to_add['category_name'],))
    category_id = cur.fetchone()

    if category_id is None:
        add_category_sql = "insert into category (name) values (%s)"
        cur.execute(add_category_sql, (product_to_add['category_name'],))
        conn.commit()

    cur.execute(check_category_query, (product_to_add['category_name'],))
    category_id = cur.fetchone()

    insert_product_sql = "insert into product (name, price, description, image_url, category_id) " \
                         "values (%s, %s, %s, %s, %s)"
    cur.execute(insert_product_sql,
                (product_to_add['name'],
                 float(product_to_add['price']),
                 product_to_add['description'],
                 product_to_add['image_url'],
                 int(category_id[0]),))
    conn.commit()

    conn.close()
    return "Product successfully added", 200
