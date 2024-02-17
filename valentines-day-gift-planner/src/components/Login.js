import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import axios from 'axios'; // Assuming you're using axios for HTTP requests

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const history = useHistory();

  const handleLogin = async () => {
    try {
      const response = await axios.post('/api/login', { email, password });
      const authToken = response.data.token;

      // Store authentication token in local storage
      localStorage.setItem('authToken', authToken);

      // Redirect to the gift list page
      history.push('/giftlist');
    } catch (error) {
      console.error('Login failed:', error);
      // Handle login error (e.g., display error message to user)
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <input type="text" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
      <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
};

export default Login;
