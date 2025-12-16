
from flask import Blueprint, request, jsonify
from core.inference import run_inference
from core.validation import validate_model
from core.explainability import explain

api = Blueprint("api", __name__)

@api.route("/health")
def health():
    return jsonify({"status": "running"})

@api.route("/infer", methods=["POST"])
def infer():
    return jsonify(run_inference(request.json.get("features", [])))

@api.route("/decision")
def decision():
    v = validate_model({})
    e = explain(v)
    return jsonify({"validation": v, "explanation": e})
