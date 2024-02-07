import React from 'react';
import { Link } from 'react-router-dom';

function HomePage() {
  return (
    <div>
      <h1>Welcome to Valentine's Day Gift Planner!</h1>
      <p>Find the perfect gifts for your loved ones.</p>
      <Link to="/gifts">View Gift List</Link>
    </div>
  );
}

export default HomePage;
