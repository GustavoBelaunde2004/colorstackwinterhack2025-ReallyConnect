import Breadcrumb from "../components/BreadCrumb";
import "../App.css";

import { useNavigate } from "react-router-dom";

const SignIn = () => {
  const navigate = useNavigate();

  const handleSignIn = () => {
    // After successful auth
    navigate("/app/home");
  };

  return (
    <div>
      <Breadcrumb />
      <h1>Sign In</h1>
      <button onClick={handleSignIn}>Sign In through Linkedin</button>
    </div>
  );
};

export default SignIn;
