import MobileNav from "../components/MobileNav";
import "../App.css";

const Matches = () => {
  return (
    <div className="matches-page">
      <h1>Your Matches</h1>

      <div className="match-list">
        <div className="match-item">
          <img src="/assets/sarah.jpg" alt="Match" />
          <div>
            <h4>Sarah Kim</h4>
            <p>Tap to message</p>
          </div>
        </div>

        <div className="match-item">
          <img src="/assets/JamesWright.jpg" alt="Match" />
          <div>
            <h4>James Wright</h4>
            <p>Tap to message</p>
          </div>
        </div>
      </div>

      <MobileNav />
    </div>
  );
};

export default Matches;
