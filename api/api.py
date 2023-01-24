from flask import Flask
#import flask_monitoringdashboard as dashboard
from api.products import products

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
#dashboard.bind(app)
app.register_blueprint(products)


@app.route("/api/version")
def version():
    return "1.0"


if __name__ == "__main__":
    app.run(debug=True)
