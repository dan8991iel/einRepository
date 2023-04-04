from products import add_product, config
import pytest
import requests
import mariadb
import json
from flask.testing import FlaskClient
from api import app

@pytest.fixture(scope="session")
def db_connection():
    conn = mariadb.connect(
        user="test_webshop",
        password="test_webshop",
        host="sep-dev.marcelstruck.de",
        port=49160,
        database="test_webshop"
    )
    yield conn
    conn.close()

def testAddProduct(db_connection):
    # Insert a test record into the database
    cur = db_connection.cursor()
    cur.execute("truncate table product")
    db_connection.commit()

    #config Werte überschreiben
    config["user"]="test_webshop"
    config["password"]="test_webshop"
    config["host"]="sep-dev.marcelstruck.de"
    config["port"]=49160
    config["database"]="test_webshop"

    with app.test_client() as client:
        client.post("/api/v1/products",json={"name":"Keks", "price":"20.00", "description":"Schoko", "image_url":"https://image.essen-und-trinken.de/13073754/t/ld/v3/w960/r1/-/schokokekse-adobestock-245097665.jpg", "category_name":"Kekse"})


    query = "select p.id, p.name, p.price, p.description, p.image_url, p.category_id FROM product p" 

    cur.execute(query)
    rv = cur.fetchall()

    # Assert that the user data matches the database record
    assert rv[0][1] == "Keks"
    assert rv[0][2] == 20.00
    assert rv[0][3] == "Schoko"
    assert rv[0][4] == "https://image.essen-und-trinken.de/13073754/t/ld/v3/w960/r1/-/schokokekse-adobestock-245097665.jpg"
    assert rv[0][5] == 1
