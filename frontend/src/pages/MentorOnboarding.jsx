// src/pages/MentorOnboarding.js
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../App.css";
import logo from "../assets/logo.png";

const MentorOnboarding = () => {
  const navigate = useNavigate();
  const [answers, setAnswers] = useState({
    expertise: "",
    adviceArea: "",
    hobby: "",
  });

  const handleChange = (e) => {
    setAnswers({ ...answers, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    localStorage.setItem("mentorOnboarding", JSON.stringify(answers));
    navigate("/app/home"); // Navigate to app home
  };

  return (
    <div className="onboarding-page">
      <h1>Mentor Onboarding</h1>
      <form onSubmit={handleSubmit} className="onboarding-form">
        <label>
          What is your area of expertise?
          <input
            type="text"
            name="expertise"
            value={answers.expertise}
            onChange={handleChange}
            required
          />
        </label>

        <label>
          Which areas do you provide guidance in?
          <input
            type="text"
            name="adviceArea"
            value={answers.adviceArea}
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

export default MentorOnboarding;
