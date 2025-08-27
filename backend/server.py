from flask import Flask
from extensions import db
from flask_cors import CORS

# initialization
app = Flask(__name__)
CORS(app)

# database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ikramkml@localhost:5432/test"
db.init_app(app)

# import models and routes
from models.survey import Survey
from routes.surveyRoutes import survey_bp

app.register_blueprint(survey_bp, url_prefix="/surveys")

# run server and create database table if not already created
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
    app.run(debug=True)

