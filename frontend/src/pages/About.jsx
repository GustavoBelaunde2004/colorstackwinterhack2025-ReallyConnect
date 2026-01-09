import "../App.css";
import Breadcrumb from "../components/BreadCrumb.jsx";

const About = () => {
  return (
    <>
      <Breadcrumb />
      <div className="about-page">
        <h1>About Us</h1>
        <p>
          Welcome to our application! We are dedicated to providing the best
          service possible.
        </p>
      </div>
    </>
  );
};

export default About;
