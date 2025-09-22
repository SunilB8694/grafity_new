from flask import Blueprint , jsonify

grafity_bp = Blueprint("Grafity", __name__, url_prefix="/Grafity")

@grafity_bp.route("/Hello", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hello, World!"})