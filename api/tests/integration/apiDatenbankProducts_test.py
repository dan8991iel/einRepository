from products import product_list, config
import pytest
import requests
import mariadb
import json


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

def testProductList(db_connection):
    # Insert a test record into the database
    cur = db_connection.cursor()
    cur.execute("truncate table product")
    cur.execute("INSERT INTO product (name, price, description, image_url, category_id) " \
                         "values ('Keks', 20.00, 'Schoko', 'https://image.essen-und-trinken.de/13073754/t/ld/v3/w960/r1/-/schokokekse-adobestock-245097665.jpg', 1)")
    db_connection.commit()

    #config Werte überschreiben
    config["user"]="test_webshop"
    config["password"]="test_webshop"
    config["host"]="sep-dev.marcelstruck.de"
    config["port"]=49160
    config["database"]="test_webshop"

    #man ruft den API Endpunkt über eine Methode auf
    response = product_list()

    # Parse(in eine Verständlche Form bringen) the response JSON
    data = json.loads(response)

    # Assert that the user data matches the database record
    assert data[0]["name"] == "Keks"
    assert data[0]["price"] == 20.00
    assert data[0]["description"] == "Schoko"
    assert data[0]["image_url"] == "https://image.essen-und-trinken.de/13073754/t/ld/v3/w960/r1/-/schokokekse-adobestock-245097665.jpg"
    assert data[0]["category_name"] == "Kekse"
