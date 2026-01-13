import "../App.css";

const ProfileCard = ({ image, name, bio }) => {
  // Use placeholder if no image provided
  const displayImage = image || "https://via.placeholder.com/400x500/cccccc/666666?text=No+Photo";

  return (
    <div className="profile-card">
      <img
        src={displayImage}
        alt={name}
        onError={(e) => {
          // Fallback if image fails to load
          e.target.src = "https://via.placeholder.com/400x500/cccccc/666666?text=No+Photo";
        }}
      />

      <div className="profile-overlay">
        <h3>{name}</h3>
        <p>{bio}</p>
      </div>
    </div>
  );
};

export default ProfileCard;
