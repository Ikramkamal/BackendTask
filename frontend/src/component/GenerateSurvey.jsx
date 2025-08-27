// This component handles user input for survey description,
// sends it to the backend for AI-generated survey questions, 
// and updates the state with the generated questions.

import React, { useState } from "react";
import PropTypes from "prop-types";

const GenerateSurvey = ({ setSurveyTitle, setQuestions, setSurveyDescription }) => {
  const [description, setDescription] = useState("");
  const [isGenerating, setIsGenerating] = useState(false);

  const handleGenerate = async () => {
    if (!description.trim()) return;

    setIsGenerating(true);

    try {
      //POST request to send survey description
      const response = await fetch("http://127.0.0.1:5000/surveys/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ description }),
      });

      const data = await response.json();

      setSurveyTitle(data.survey.title);
      setSurveyDescription(data.description);
      setQuestions(
        //Formating the genrated questions to follow frontend struture
        (data.survey.questions || []).map((q, i) => {
          const typeMap = {
            "short answer": "shortAnswer",
            "long answer": "openQuestion",
            "single choice": "singleChoice",
            "multiple choice": "multipleChoice",
            "rating": "scale",
            "nps": "npsScore",
        };

        return {
          id: i.toString(),
          title: q.text ?? "",
          type: typeMap[q.type] ?? "shortAnswer",
          options: (q.options || []).map((opt, j) => ({
            id: `${i}-${j}`,     
            text: opt,          
          })),
          saved: true,
        };
      })
    );
      setDescription("");
    } 
    
    catch (error) {
      console.error("Error generating survey:", error);
      alert("Something went wrong while generating the survey.");
    } 
    
    finally {
      setIsGenerating(false);
    }
  };

  return (
    <div className="flex gap-2 items-center">
      <input
        type="text"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        placeholder="Describe your survey..."
        className="p-2 border border-gray-300 rounded-md flex-1"
        disabled={isGenerating}
      />
      <button
        onClick={handleGenerate}
        disabled={isGenerating}
        className="px-4 py-2 bg-[#6851a7] text-white rounded-md"
      >
        {isGenerating ? "Generating..." : "Generate"}
      </button>
    </div>
  );
};

GenerateSurvey.propTypes = {
  setSurveyTitle: PropTypes.func.isRequired,
  setQuestions: PropTypes.func.isRequired,
  setSurveyDescription: PropTypes.func.isRequired,
};

export default GenerateSurvey;
