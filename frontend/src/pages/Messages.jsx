import MobileNav from "../components/MobileNav";
import "../App.css";
import { useNavigate } from "react-router-dom";

const name = "James Wright";

const Messages = () => {
  const navigation = useNavigate();

  return (
    <div className="matches-page">
      <div className="messages-header">
        <p
          className="messages-back"
          onClick={() => navigation("/app/matches")}
          style={{ cursor: "pointer", color: "#fff" }}
        >
          &larr; Back
        </p>
        <h2 style={{ color: "#fff", margin: 0 }}>{name}</h2>
      </div>

      {/* Messages content area */}
      <div style={{
        marginTop: "2rem",
        marginBottom: "8rem",
        minHeight: "50vh",
        color: "#fff"
      }}>
        <p style={{ textAlign: "center", color: "#ccc", fontSize: "0.9rem" }}>
          No messages yet. Start the conversation!
        </p>
        {/* Future: Render actual messages here */}
      </div>

      <div className="message-textbox-container">
        <input
          type="text"
          placeholder="Send a message..."
          className="message-textbox"
        />
        <button className="message-send-button">Send</button>
      </div>
      <MobileNav />
    </div>
  );
};

export default Messages;
