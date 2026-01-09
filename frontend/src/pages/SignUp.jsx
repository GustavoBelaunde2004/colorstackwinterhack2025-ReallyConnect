import Breadcrumb from "../components/BreadCrumb";

import "../App.css";
import Card from "../components/Card";

const SignUp = () => {
  return (
    <div className="sign-up">
      <Breadcrumb />
      <h1>Sign up</h1>
      <Card image="https://via.placeholder.com/150" name="Mentor" />
      <Card image="https://via.placeholder.com/150" name="Mentee" />
    </div>
  );
};

export default SignUp;
