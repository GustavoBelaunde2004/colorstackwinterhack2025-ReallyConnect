import { Link, useLocation } from "react-router-dom";
import "../App.css";

const Breadcrumb = () => {
  const location = useLocation();
  const pathnames = location.pathname.split("/").filter(Boolean);

  return (
    <nav className="breadcrumb">
      <Link to="/">Home</Link>

      {pathnames.map((name, index) => {
        const routeTo = "/" + pathnames.slice(0, index + 1).join("/");

        return (
          <span key={index}>
            <span className="breadcrumb-separator">›</span>
            <Link to={routeTo}>
              {name.charAt(0).toUpperCase() + name.slice(1)}
            </Link>
          </span>
        );
      })}
    </nav>
  );
};

export default Breadcrumb;
