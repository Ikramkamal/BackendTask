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
            f"Generate a survey in JSON format based on this description: {description}, "
            f"follow format: {{ \"title\": \"...\", \"questions\": [ "
            f"{{ \"type\": \"...\", \"text\": \"...\" }}, … ] }}"
        )
    )

    text = response.text.strip()

    # # Remove triple backticks if present
    # if text.startswith("```") and text.endswith("```"):
    #     text = text[3:-3].strip()

    print(text)


    try:
        survey_json = json.loads(text)
    except json.JSONDecodeError:

        title_match = re.search(r'"title"\s*:\s*"([^"]+)"', text)
        title = title_match.group(1) if title_match else description

   
         # Extract questions with type and text
        question_matches = re.findall(
            r'\{\s*"type"\s*:\s*"([^"]+)"\s*,\s*"text"\s*:\s*"([^"]+)"\s*\}', 
            text
        )

        # Build questions list
        questions = [{"type": qtype, "text": qtext} for qtype, qtext in question_matches]

        survey_json = {
            "title": title,
            "questions": questions
        }



    survey_json.setdefault("title", description)
    survey_json.setdefault("questions", [])

    return survey_json
