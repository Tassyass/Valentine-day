import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; // Import Routes instead of BrowserRouter and Route
import LoginForm from './Auth/LoginForm';
import HomePage from './components/HomePage';
import GiftListPage from './components/GiftListPage';

const App = () => {
  const [user, setUser] = useState(null);

  const handleLogin = (userData) => {
    // Logic for handling login
    setUser(userData);
  };

  const handleLogout = () => {
    // Logic for handling logout
    setUser(null);
  };

  return (
    <Router>
      <div style={{ backgroundColor: '#f0f0f0', minHeight: '100vh', padding: '20px' }}>
        <h1 style={{ textAlign: 'center', marginBottom: '20px' }}>Valentine's Gift Planner</h1>
        
        {/* Use Routes component instead of Switch */}
        <Routes>
          {/* Route for login page */}
          <Route path="/login" element={<LoginForm handleLogin={handleLogin} />} />
          
          {/* Route for gift list page */}
          <Route path="/giftlist" element={<GiftListPage user={user} handleLogout={handleLogout} />} />
          
          {/* Default route for home page */}
          <Route path="/" element={<HomePage />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
