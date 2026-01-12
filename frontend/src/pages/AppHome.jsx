import ProfileCard from "../components/ProfileCard";
import MobileNav from "../components/MobileNav";
import sarah from "../assets/sarah.jpg";
import "../App.css";

const mockProfiles = [
  {
    name: "Sarah Kim",
    bio: "Product Manager • 6 yrs experience",
    image: { sarah },
  },
];

const AppHome = () => {
  return (
    <div className="app-home-page">
      {mockProfiles.map((p, i) => (
        <ProfileCard key={i} {...p} className="profile-card" />
      ))}
      <button className="dislike-button">&#10006;</button>
      <button className="like-button">&#10004;</button>

      <MobileNav />
    </div>
  );
};

export default AppHome;
