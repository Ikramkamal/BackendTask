from flask import Blueprint, request, jsonify
from extensions import db
from models.survey import Survey

survey_bp = Blueprint("surveys", __name__)

@survey_bp.route("/generate", methods=["POST"])
def generate_survey():
    data = request.get_json()
    description = data.get("description")

    if not description:
        return jsonify({"error": "Description is required"}), 400

    existing = Survey.query.filter_by(description=description).first()
    if existing:
        return jsonify({
            "description": existing.description,
            "survey": existing.survey_json,
            "cached": True
        })

    generated = {"title": "", "questions": []}
    new_survey = Survey(description=description, survey_json=generated)
    db.session.add(new_survey)
    db.session.commit()

    return jsonify({"description": description, "survey": generated, "cached": False})
