import ProfileCard from "../components/ProfileCard";
import MobileNav from "../components/MobileNav";

const mockProfiles = [
  {
    name: "Sarah Kim",
    bio: "Product Manager • 6 yrs experience",
    image: "/assets/profile1.jpg",
  },
  {
    name: "James Wright",
    bio: "Software Engineer • AWS Certified",
    image: "/assets/profile2.jpg",
  },
];

const AppHome = () => {
  return (
    <div
      style={{
        backgroundImage: "url('/assets/landing.jpeg')",
        paddingBottom: "80px",
      }}
    >
      {mockProfiles.map((p, i) => (
        <ProfileCard key={i} {...p} />
      ))}

      <MobileNav />
    </div>
  );
};

export default AppHome;
