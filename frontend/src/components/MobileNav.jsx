import { NavLink } from "react-router-dom";
import { FaHome, FaUser, FaComments } from "react-icons/fa";

import "../App.css";
import Breadcrumb from "./BreadCrumb";

const MobileNav = () => {
  return (
    <nav className="mobile-nav">
      <NavLink to="/app/matches" className="nav-item">
        <FaComments />
        <span>Matches</span>
      </NavLink>
      <NavLink to="/app/home" className="nav-item">
        <FaHome />
        <span>Home</span>
      </NavLink>
      <NavLink to="/app/profile" className="nav-item">
        <FaUser />
        <span>Profile</span>
      </NavLink>
    </nav>
  );
};

export default MobileNav;
