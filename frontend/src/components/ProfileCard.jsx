import "../App.css";

const ProfileCard = ({ image, name, bio }) => {
  return (
    <div className="profile-card">
      <img src={image} alt={name} />

      <div className="profile-overlay">
        <h3>{name}</h3>
        <p>{bio}</p>
      </div>
    </div>
  );
};

export default ProfileCard;
