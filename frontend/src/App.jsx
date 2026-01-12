import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Landing from "./pages/Landing";
import SignIn from "./pages/SignIn";
import SignUp from "./pages/SignUp";

import MentorOnboarding from "./pages/MentorOnboarding";
import MenteeOnboarding from "./pages/MenteeOnboarding";

import AppHome from "./pages/AppHome";
import Matches from "./pages/Matches";
import Messages from "./pages/Messages";

import Profile from "./pages/Profile";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Public */}
        <Route path="/" element={<Landing />} />
        <Route path="/signin" element={<SignIn />} />
        <Route path="/signup" element={<SignUp />} />

        {/* Onboarding flows */}
        <Route path="/signup/mentor" element={<MentorOnboarding />} />
        <Route path="/signup/mentee" element={<MenteeOnboarding />} />

        {/* Post-auth App */}
        <Route path="/app/home" element={<AppHome />} />
        <Route path="/app/matches" element={<Matches />} />
        <Route path="/app/matches/messages" element={<Messages />} />
        <Route path="/app/profile" element={<Profile />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
