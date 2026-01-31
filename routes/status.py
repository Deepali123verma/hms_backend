from flask import Blueprint, jsonify

# Blueprint create karo
bp = Blueprint("status", __name__)

# /api/status endpoint
@bp.route("/status")
def status():
    return jsonify({"status": "ok", "message": "Hotel Management API is running"})

