import "../App.css";

const Card = (props) => {
  return (
    <>
      <div className="card" onClick={props.onClick}>
        <img src={props.image} alt={props.title} />
        <h2>{props.title}</h2>
      </div>
    </>
  );
};

export default Card;
