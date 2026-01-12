import MobileNav from "../components/MobileNav";
import "../App.css";
import { useNavigate } from "react-router-dom";

const Messages = () => {
  const navigation = useNavigate();

  return (
    <div className="matches-page">
      <p onClick={() => navigation("/matches")}>Back</p>
      <h2>Profile</h2>

      <input
        type="text"
        placeholder="Search messages..."
        className="message-search"
      />
      <MobileNav />
    </div>
  );
};

export default Messages;
