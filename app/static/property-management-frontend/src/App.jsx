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
import PaymentsPage from './pages/PaymentsPage';
import AvailabilityPage from './pages/AvailabilityPage';
import ViewApartmentsPage from './pages/ViewApartmentsPage';

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
          <Route path="/Payments" element={<PaymentsPage />} />
          <Route path="/Availability" element={<AvailabilityPage />} />
          <Route path="/ViewApartments" element={<ViewApartmentsPage />} />
        </Routes>
    </BrowserRouter>
  );
};

export default App;
