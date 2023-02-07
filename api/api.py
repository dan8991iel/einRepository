from flask import Flask, request
#import flask_monitoringdashboard as dashboard
from products import products
from categories import categories
from flask_cors import CORS
from flask_firebase_admin import FirebaseAdmin

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
#dashboard.bind(app)
app.register_blueprint(products)
app.register_blueprint(categories)
CORS(app)
firebase = FirebaseAdmin(app)

@app.route("/api/version")
def version():
    return "1.0"

@app.route('/api/v1/whoami', methods=['GET'])
@firebase.jwt_required
def whoami():
    return {"message": f"Hello {request.jwt_payload['email']}!", "paload": request.jwt_payload}

if __name__ == "__main__":
    app.run(debug=True)
