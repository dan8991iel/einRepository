import os
import pymysql
from dotenv import load_dotenv
from flask import Blueprint
from flask import request, jsonify

load_dotenv()

orders = Blueprint('orders', __name__)

config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'database': os.getenv('DB_NAME')
}


@orders.route('/api/v1/orders', methods=['POST'])
def add_order():
    order = request.get_json(force=True)

    conn = pymysql.connect(**config)
    cur = conn.cursor()

    insert_order_sql = "insert into webshop.order (name, email, ordertotal, street, house_number, zipcode, " \
                       "city) values (%s, %s, %s, %s, %s, %s, %s)"

    cur.execute(insert_order_sql,
                (order['name'],
                 order['email'],
                 float(order['ordertotal']),
                 order['street'],
                 order['house_number'],
                 order['zipcode'],
                 order['city'],))
    order_id = cur.lastrowid
    for i in range(len(order['products'])):
        insert_orderposition_sql = "insert into webshop.orderposition (order_id, product_id, quantity) " \
                                   "values (%s, %s, %s)"
        cur.execute(insert_orderposition_sql, (order_id, order['products'][i]['id'], order['products'][i]['quantity'],))
    conn.commit()
    conn.close()
    return "Order was created", 200
