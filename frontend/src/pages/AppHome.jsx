import ProfileCard from "../components/ProfileCard";
import MobileNav from "../components/MobileNav";

const mockProfiles = [
  {
    name: "Sarah Kim",
    bio: "Product Manager • 6 yrs experience",
    image: "../assets/sarah.jpg",
  },
];

const AppHome = () => {
  return (
    <div className="app-home-page">
      {mockProfiles.map((p, i) => (
        <ProfileCard key={i} {...p} className="profile-card" />
      ))}

      <MobileNav />
    </div>
  );
};

export default AppHome;
