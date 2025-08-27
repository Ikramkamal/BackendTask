# Logic integration for survey generation using Google GenAI API
# This module handles the interaction with the Google GenAI API 
# to generate survey questions based on a textual description.

import json
import re
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.environ.get("API_KEY"))

def generate_survey_from_description(description: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=(
            f"Generate a survey in strict JSON format based on this description: {description}. "
            f"Format: {{ "
            f"\"title\": \"...\", "
            f"\"questions\": [ "
            f"{{ \"type\": \"...\", \"text\": \"...\", \"options\": [\"...\"] (if applicable) }}, … "
            f"] "
            f"}}. "
            f"Allowed question types are only: "
            f"['single choice', 'multiple choice', 'long answer', 'short answer', 'rating']. "
            f"Do not use any other type."
        )
    )

    text = response.text.strip()

    # Clean generated response to follow JSON format
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?", "", text)
        text = re.sub(r"```$", "", text)
        text = text.strip()
    print(text)


    survey_json = json.loads(text)

    survey_json.setdefault("title", description)
    survey_json.setdefault("questions", [])

    return survey_json
