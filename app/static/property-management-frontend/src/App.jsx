// App.jsx
import React from 'react';
import { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, BrowserRouter } from 'react-router-dom';
import Navbar from './components/Navbar';
import LandingPage from './pages/LandingPage';
import SignUp from './pages/SignUpPage';
import SignIn from './pages/SignInPage';
import UserDashboardPage from './pages/UserDashboardPage';
import AdminDashboardPage from './pages/AdminDashboardPage';

const App = () => {
  return (
    <BrowserRouter>
      <Navbar />

        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/signup" element={<SignUp />} />
          <Route path="/signin" element={<SignIn />} />
          <Route path="/UserDashboard" element={<UserDashboardPage />} />
          <Route path="/AdminDashboard" element={<AdminDashboardPage />} />
        </Routes>
    </BrowserRouter>
  );
};

export default App;
