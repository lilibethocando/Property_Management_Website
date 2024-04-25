// App.jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import TopSection from './components/TopSection';
import FeatureSection from './components/FeatureSection';
import SignUp from './components/SignUp'; 

const App = () => {
  return (
    <Router>
      <Navbar />
      <div className="max-w-7xl mx-auto pt-20 px-6">
        <TopSection /> {/* Add TopSection component */}
        <Routes>
          <Route path="/" element={<TopSection />} />
          <Route path="/signup" element={<SignUp />} />
        </Routes>
        <FeatureSection />
      </div>
    </Router>
  );
};

export default App;
