import { useNavigate } from "react-router-dom";
import MobileNav from "../components/MobileNav";
import "../App.css";

const Profile = () => {
  const navigate = useNavigate();

  const handleSignOut = () => {
    // Optional: clear auth/session data
    localStorage.clear();

    navigate("/"); // back to landing or /signin
  };

  return (
    <div className="profile-page">
      <h1>Your Profile</h1>

      <button className="signout-btn" onClick={handleSignOut}>
        Sign Out
      </button>

      <MobileNav />
    </div>
  );
};

export default Profile;
