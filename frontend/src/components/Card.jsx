import "../App.css";

import Nav from "../components/Nav.jsx";

const Card = (props) => {
  return (
    <>
      <div className="card">
        <img src={props.image} alt={props.name} />
        <h2>{props.name}</h2>
        <p>
          {props.role}@{props.company}
        </p>
      </div>
    </>
  );
};

export default Card;
