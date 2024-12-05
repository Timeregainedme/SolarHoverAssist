from flask import Blueprint, jsonify

api = Blueprint("api", __name__)

@api.route("/status", methods=["GET"])
def get_status():
    return jsonify({"status": "Server is running"})
