import React, { useState } from "react";
import PropTypes from "prop-types";

const GenerateSurveyButtonAndPrompt = ({ setSurveyTitle, setQuestions, setSurveyDescription }) => {
  const [description, setDescription] = useState("");
  const [isGenerating, setIsGenerating] = useState(false);

  const handleGenerate = async () => {
    if (!description.trim()) return;

    setIsGenerating(true);

    try {
      const response = await fetch("http://127.0.0.1:5000/surveys/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ description }),
      });

      const data = await response.json();

      setSurveyTitle(data.survey.title);
      setSurveyDescription(data.description);
      setQuestions(data.survey.questions);

      setDescription("");
    } catch (error) {
      console.error("Error generating survey:", error);
      alert("Something went wrong while generating the survey.");
    } finally {
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

GenerateSurveyButtonAndPrompt.propTypes = {
  setSurveyTitle: PropTypes.func.isRequired,
  setQuestions: PropTypes.func.isRequired,
  setSurveyDescription: PropTypes.func.isRequired,
};

export default GenerateSurveyButtonAndPrompt;
