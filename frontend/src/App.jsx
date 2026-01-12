import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Landing from "./pages/Landing";
import SignIn from "./pages/SignIn";
import SignUp from "./pages/SignUp";
import AppHome from "./pages/AppHome";
import Matches from "./pages/Matches";
import Profile from "./pages/Profile";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Public */}
        <Route path="/" element={<Landing />} />
        <Route path="/signin" element={<SignIn />} />
        <Route path="/signup" element={<SignUp />} />

        {/* Post-auth App */}
        <Route path="/app/home" element={<AppHome />} />
        <Route path="/app/matches" element={<Matches />} />
        <Route path="/app/profile" element={<Profile />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
