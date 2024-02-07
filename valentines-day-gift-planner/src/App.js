import React from 'react';
import { BrowserRouter as Router, Route} from 'react-router-dom';
import { Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import GiftListPage from './pages/GiftListPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" component={<HomePage />} />
        <Route path="/gifts" component={<GiftListPage />} />
        <Routes></Routes>
      </Routes>
    </Router>
  );
}

export default App;
