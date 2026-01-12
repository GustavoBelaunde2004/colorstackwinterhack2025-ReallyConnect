import MobileNav from "../components/MobileNav";
import "../App.css";
import { useNavigate } from "react-router-dom";

const name = "James Wright";

const Messages = () => {
  const navigation = useNavigate();

  return (
    <div className="matches-page">
      <p className="messages-back" onClick={() => navigation("/app/matches")}>
        {" "}
        &larr; Back
      </p>
      <h2>{name}</h2>

      <div className="message-textbox-container">
        <input
          type="text"
          placeholder=":Send a message..."
          className="message-textbox"
        />{" "}
        <button className="message-send-button">Send</button>
      </div>
      <MobileNav />
    </div>
  );
};

export default Messages;
