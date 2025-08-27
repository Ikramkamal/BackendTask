from flask import Flask
from extensions import db

from flask_cors import CORS



app = Flask(__name__)

CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ikramkml@localhost:5432/test"

db.init_app(app)


from routes.surveyRoutes import survey_bp
app.register_blueprint(survey_bp, url_prefix="/surveys")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()   # ensures tables are created
    app.run(debug=True)

