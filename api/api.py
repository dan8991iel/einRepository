from flask import Flask, request
# import flask_monitoringdashboard as dashboard
from products import products
from categories import categories
from flask_cors import CORS
from flask_firebase_admin import FirebaseAdmin
from firebase_admin import auth

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
# dashboard.bind(app)
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
    uid = request.jwt_payload['uid']
    user = auth.get_user(uid=uid)
    role = user.custom_claims["role"]
    return {"message": f"Hello {request.jwt_payload['email']}!", "payload": request.jwt_payload, "role": role}


@app.route('/api/v1/escalatePrivileges', methods=['GET'])
@firebase.jwt_required
def escalate_privileges():
    uid = request.jwt_payload['uid']
    user = auth.get_user(uid=uid)
    custom_claims = user.custom_claims
    custom_claims["role"] = "admin"

    auth.set_custom_user_claims(uid=uid, custom_claims=custom_claims)
    return {"message": f"You are now admin", "payload": request.jwt_payload}


if __name__ == "__main__":
    app.run(debug=True)
