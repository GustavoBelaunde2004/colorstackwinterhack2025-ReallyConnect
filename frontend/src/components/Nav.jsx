import "../App.css";
import logo from "../assets/logo.png";

const Nav = () => {
  return (
    <nav className="landing-nav">
      <a href="/">
        <img src={logo} alt="Logo" className="nav-logo" />
      </a>
      <ul className="horizontal-list">
        <li>
          <a href="/signin">
            Sign In with{" "}
            <img src="../assets/linkedin-logo.png" alt="Linkedin" />
          </a>
        </li>
        <li>
          <a href="/signup">Sign Up</a>
        </li>
      </ul>
    </nav>
  );
};

export default Nav;
