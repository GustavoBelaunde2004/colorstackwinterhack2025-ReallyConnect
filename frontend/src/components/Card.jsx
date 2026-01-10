import "../App.css";

import Nav from "../components/Nav.jsx";

const Card = (props) => {
  return (
    <>
      <div className="card">
        <img src={props.image} alt={props.title} />
        <h2>{props.title}</h2>
        <h4>
          Sign Up with <img src="../assets/linkedin-logo.png" alt="Linkedin" />
        </h4>
      </div>
    </>
  );
};

export default Card;
