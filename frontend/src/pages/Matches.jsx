import MobileNav from "../components/MobileNav";
import "../App.css";

import profile from "../assets/JamesWright.jpg";

const Matches = () => {
  return (
    <div className="matches-page">
      <h1>Your Matches</h1>

      <div className="match-list">
        <a className="match-message" href="/app/matches/messages">
          <div className="match-item">
            <img src={profile} alt="Match" />
            <div>
              <h4>James Wright</h4>
              <p>Tap to message</p>
            </div>
          </div>
        </a>
      </div>
      <MobileNav />
    </div>
  );
};

export default Matches;
