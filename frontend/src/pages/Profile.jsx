import { useNavigate } from "react-router-dom";
import { useState } from "react";
import MobileNav from "../components/MobileNav";
import "../App.css";

const Profile = () => {
  const navigate = useNavigate();

  // Initialize state directly from localStorage
  const initialProfile = JSON.parse(localStorage.getItem("profile")) || {
    name: "John Doe",
    email: "john@example.com",
    careergoals: "Software Engineer",
    hobbies: "Hiking",
  };
  const [profile, setProfile] = useState(initialProfile);
  const [editMode, setEditMode] = useState(false);

  // Handle Sign Out
  const handleSignOut = () => {
    localStorage.clear();
    navigate("/"); // back to landing or /signin
  };

  // Handle Update
  const handleUpdate = () => {
    localStorage.setItem("profile", JSON.stringify(profile));
    setEditMode(false);
  };

  // Handle Delete
  const handleDelete = () => {
    localStorage.removeItem("profile");
    setProfile({ name: "", email: "" });
    alert("Profile deleted!");
  };

  // Handle input changes
  const handleChange = (e) => {
    setProfile({ ...profile, [e.target.name]: e.target.value });
  };

  return (
    <div className="profile-page">
      <h1>My Profile</h1>

      <div className="profile-info">
        <div>
          <strong>Name:</strong>
          {editMode ? (
            <input
              className="profile-input"
              type="text"
              name="name"
              value={profile.name}
              onChange={handleChange}
            />
          ) : (
            <span>{profile.name}</span>
          )}
        </div>

        <div>
          <strong>Email:</strong>
          {editMode ? (
            <input
              className="profile-input"
              type="email"
              name="email"
              value={profile.email}
              onChange={handleChange}
            />
          ) : (
            <span>{profile.email}</span>
          )}
        </div>
        <div>
          <strong>Career Goals:</strong>
          {editMode ? (
            <input
              className="profile-input"
              type="text"
              name="careergoals"
              value={profile.careergoals}
              onChange={handleChange}
            />
          ) : (
            <span>{profile.careergoals}</span>
          )}
        </div>
        <div>
          <strong>Hobbies:</strong>
          {editMode ? (
            <input
              className="profile-input"
              type="text"
              name="hobbies"
              value={profile.hobbies}
              onChange={handleChange}
            />
          ) : (
            <span>{profile.hobbies}</span>
          )}
        </div>

        <div style={{ marginTop: "1rem" }}>
          {editMode ? (
            <button className="update-btn" onClick={handleUpdate}>
              Save
            </button>
          ) : (
            <button className="update-btn" onClick={() => setEditMode(true)}>
              Edit
            </button>
          )}

          <button className="delete-btn" onClick={handleDelete}>
            Delete
          </button>
        </div>
      </div>

      <button className="signout-btn" onClick={handleSignOut}>
        Sign Out
      </button>

      <MobileNav />
    </div>
  );
};

export default Profile;
