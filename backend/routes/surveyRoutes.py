from flask import Blueprint, request, jsonify
from extensions import db
from models.survey import Survey
from services.surveyGenerator import generate_survey_from_description  

# Blueprint for survey-related routes
survey_bp = Blueprint("surveys", __name__)

@survey_bp.route("/generate", methods=["POST"])

def generate_survey():
   
    data = request.get_json()
    description = data.get("description")

    if not description:
        return jsonify({"error": "Description is required"}), 400

    # Check if survey already exists in DB
    existing = Survey.query.filter_by(description=description).first()
    if existing:
        # If exists, return cached result
        return jsonify({
            "description": existing.description,
            "survey": existing.survey_json,
            "cached": True
        })

    try:
        generated_survey = generate_survey_from_description(description)

    except Exception as e:
        print(f"Error generating survey: {str(e)}")
        return jsonify({"error": str(e)}), 500

    # Save to DB
    new_survey = Survey(description=description, survey_json=generated_survey)
    db.session.add(new_survey)
    db.session.commit()

    print("Survey response:", generated_survey)

    return jsonify({
        "description": description,
        "survey": generated_survey,
        "cached": False
    })
