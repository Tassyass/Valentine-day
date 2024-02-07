import React from 'react';
import ReactDOM from 'react-dom';
import HomePage from './components/HomePage';

ReactDOM.render(
  <React.StrictMode>
    <HomePage />
  </React.StrictMode>,
  document.getElementById('root') // This should match the id of the root element in index.html
);
