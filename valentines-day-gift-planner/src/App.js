import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import GiftListPage from './pages/GiftListPage';

function App() {
  // Define a login component inline
  const Login = () => {
    // Handler for login button click
    const handleLogin = () => {
      // Add your login logic here
      console.log("Logging in...");
    };

    return (
      <div>
        <h2>Login Page</h2>
        <form>
          <div>
            <label htmlFor="email">Email:</label>
            <input type="email" id="email" name="email" />
          </div>
          <div>
            <label htmlFor="username">Username:</label>
            <input type="text" id="username" name="username" />
          </div>
          <button type="button" onClick={handleLogin}>Login</button>
        </form>
      </div>
    );
  };

  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<HomePage />} />
        <Route path="/gifts" element={<GiftListPage />} />
        {/* Add login route */}
        <Route path="/login" element={<Login />} />
      </Routes>
    </Router>
  );
}

export default App;
