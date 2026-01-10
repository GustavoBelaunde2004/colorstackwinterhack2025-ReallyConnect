import Breadcrumb from "../components/BreadCrumb";
import { useNavigate } from "react-router-dom";
import Card from "../components/Card";
import mentorImg from "../assets/mentor.webp";
import menteeImg from "../assets/mentee.jpg";

import "../App.css";

const SignUp = () => {
  const navigate = useNavigate();

  return (
    <>
      <Breadcrumb />
      <div className="role-page">
        <h1 className="role-title">Choose Your Role</h1>

        <div className="role-card-container">
          <Card
            title="Mentor"
            image={mentorImg}
            onClick={() => navigate("/signup/mentor")}
          />

          <Card
            title="Mentee"
            image={menteeImg}
            onClick={() => navigate("/signup/mentee")}
          />
        </div>
      </div>
    </>
  );
};

export default SignUp;
