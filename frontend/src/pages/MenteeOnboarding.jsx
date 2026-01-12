// src/pages/MenteeOnboarding.js
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../App.css";

import logo from "../assets/logo.png";

const MenteeOnboarding = () => {
  const navigate = useNavigate();
  const [answers, setAnswers] = useState({
    goal1: "",
    goal2: "",
    hobby: "",
  });

  const handleChange = (e) => {
    setAnswers({ ...answers, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    localStorage.setItem("menteeOnboarding", JSON.stringify(answers));
    navigate("/app/home"); // Navigate to app home
  };

  return (
    <div className="onboarding-page">
      <h1>Mentee Onboarding</h1>
      <form onSubmit={handleSubmit} className="onboarding-form">
        <label>
          What is your primary professional goal?
          <input
            type="text"
            name="goal1"
            value={answers.goal1}
            onChange={handleChange}
            required
          />
        </label>

        <label>
          What is another goal you are working towards?
          <input
            type="text"
            name="goal2"
            value={answers.goal2}
            onChange={handleChange}
            required
          />
        </label>

        <label>
          What are your hobbies or interests?
          <input
            type="text"
            name="hobby"
            value={answers.hobby}
            onChange={handleChange}
            required
          />
        </label>

        <button type="submit" className="submit-btn">
          Complete Onboarding
        </button>
      </form>
      <img src={logo} alt="Logo" className="onboarding-logo" />
    </div>
  );
};

export default MenteeOnboarding;
