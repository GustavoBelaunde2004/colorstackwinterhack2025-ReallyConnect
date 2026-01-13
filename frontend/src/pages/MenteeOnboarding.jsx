// src/pages/MenteeOnboarding.js
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { menteeAPI, interestsAPI } from "../lib/api";
import { useAuth } from "../contexts/AuthContext";
import ImageUpload from "../components/ImageUpload";
import "../App.css";

import logo from "../assets/logo.png";

const MenteeOnboarding = () => {
  const navigate = useNavigate();
  const { refreshProfile } = useAuth();
  const [availableInterests, setAvailableInterests] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const [formData, setFormData] = useState({
    industry: "",
    goals: "",
    background: "",
    help_needed: [],
    interest_ids: [],
    profile_picture_url: "",
  });

  // Check if profile already exists and fetch interests
  useEffect(() => {
    const checkProfileAndFetchInterests = async () => {
      try {
        // Check if mentee profile already exists
        await menteeAPI.getMe();
        // Profile exists, redirect to app home
        navigate("/app/home");
      } catch (err) {
        // Profile doesn't exist (404), proceed with onboarding
        if (err.status === 404) {
          // Fetch interests for the form
          try {
            const interests = await interestsAPI.getAll();
            setAvailableInterests(interests);
          } catch (interestErr) {
            console.error("Error fetching interests:", interestErr);
          }
        } else {
          console.error("Error checking mentee profile:", err);
        }
      }
    };
    checkProfileAndFetchInterests();
  }, [navigate]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleHelpTypeChange = (helpType) => {
    setFormData((prev) => ({
      ...prev,
      help_needed: prev.help_needed.includes(helpType)
        ? prev.help_needed.filter((type) => type !== helpType)
        : [...prev.help_needed, helpType],
    }));
  };

  const handleInterestChange = (interestId) => {
    setFormData((prev) => ({
      ...prev,
      interest_ids: prev.interest_ids.includes(interestId)
        ? prev.interest_ids.filter((id) => id !== interestId)
        : [...prev.interest_ids, interestId],
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      // Create mentee profile in backend
      await menteeAPI.createMe(formData);

      // Refresh profile in auth context
      await refreshProfile();

      // Navigate to app home
      navigate("/app/home");
    } catch (err) {
      console.error("Error creating mentee profile:", err);
      setError(err.message || "Failed to create mentee profile");
      setLoading(false);
    }
  };

  const helpTypes = [
    { value: "resume_review", label: "Resume Review" },
    { value: "mock_interview", label: "Mock Interview" },
    { value: "career_advice", label: "Career Advice" },
    { value: "social_advice", label: "Social Advice" },
  ];

  const industries = [
    "Engineering",
    "Natural Sciences",
    "Formal Sciences",
    "Health Sciences",
    "Social Sciences",
    "Humanities",
    "Arts",
    "Business",
    "Education",
    "Law",
    "Communication & Media",
    "Architecture & Design",
  ];

  return (
    <div className="onboarding-page">
      <h1>Mentee Onboarding</h1>

      {error && (
        <div style={{ color: "red", marginBottom: "1rem", textAlign: "center" }}>
          {error}
        </div>
      )}

      <form onSubmit={handleSubmit} className="onboarding-form">
        <label>
          Industry
          <select
            name="industry"
            value={formData.industry}
            onChange={handleChange}
            required
            style={{
              width: "100%",
              padding: "0.5rem",
              fontSize: "1rem",
              borderRadius: "4px",
              border: "1px solid #ccc",
            }}
          >
            <option value="">Select an industry...</option>
            {industries.map((industry) => (
              <option key={industry} value={industry}>
                {industry}
              </option>
            ))}
          </select>
        </label>

        <label>
          Professional Goals
          <textarea
            name="goals"
            value={formData.goals}
            onChange={handleChange}
            placeholder="What are you hoping to achieve?"
            rows="3"
            required
          />
        </label>

        <label>
          Background
          <textarea
            name="background"
            value={formData.background}
            onChange={handleChange}
            placeholder="Tell us about your experience and where you are in your career"
            rows="3"
            required
          />
        </label>

        <label>
          Profile Picture
          <ImageUpload
            currentImageUrl={formData.profile_picture_url}
            onUploadComplete={(url) => {
              setFormData({...formData, profile_picture_url: url});
            }}
            onError={(err) => setError(err)}
            maxSizeMB={2}
          />
          <small style={{ color: "#666", fontSize: "0.85rem", marginTop: "0.25rem", display: "block" }}>
            Optional: Upload a profile picture (max 2MB)
          </small>
        </label>

        <label>
          Help I'm Looking For (Select all that apply)
          <div style={{ display: "flex", flexDirection: "column", gap: "0.5rem", marginTop: "0.5rem" }}>
            {helpTypes.map((type) => (
              <label key={type.value} style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}>
                <input
                  type="checkbox"
                  checked={formData.help_needed.includes(type.value)}
                  onChange={() => handleHelpTypeChange(type.value)}
                />
                {type.label}
              </label>
            ))}
          </div>
        </label>

        <label>
          My Interests (Select at least 3)
          <div style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fill, minmax(150px, 1fr))",
            gap: "0.5rem",
            marginTop: "0.5rem",
            maxHeight: "200px",
            overflowY: "auto",
            padding: "0.5rem",
            border: "1px solid #ccc",
            borderRadius: "4px"
          }}>
            {availableInterests.map((interest) => (
              <label key={interest.id} style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}>
                <input
                  type="checkbox"
                  checked={formData.interest_ids.includes(interest.id)}
                  onChange={() => handleInterestChange(interest.id)}
                />
                <span style={{ fontSize: "0.9rem" }}>{interest.name}</span>
              </label>
            ))}
          </div>
        </label>

        <button
          type="submit"
          className="submit-btn"
          disabled={loading || formData.help_needed.length === 0 || formData.interest_ids.length < 3}
        >
          {loading ? "Creating Profile..." : "Complete Onboarding"}
        </button>
      </form>
      <img src={logo} alt="Logo" className="onboarding-logo" />
    </div>
  );
};

export default MenteeOnboarding;
