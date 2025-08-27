from extensions import db
from sqlalchemy.dialects.postgresql import JSON

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, unique=True, nullable=False)
    survey_json = db.Column(JSON, nullable=False)
