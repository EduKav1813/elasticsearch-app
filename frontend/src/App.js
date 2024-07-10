import React, { useState } from 'react';
import { FaSearch } from 'react-icons/fa';
import './App.css';

const SearchPage = () => {
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearchInputChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleSearchSubmit = () => {
    // TODO: Handle search logic here (e.g., fetching data based on searchTerm)
    console.log('Searching for:', searchTerm);
  };

  return (
    <div className="search-page">
      <h1 className="header">Famous Quotes</h1>
      <div className="search-container">
        <div className="search-bar">
          <input
            type="text"
            placeholder="Search..."
            value={searchTerm}
            onChange={handleSearchInputChange}
            className="search-input"
          />
          <button
            onClick={handleSearchSubmit}
            className="search-button"
          >
            <FaSearch style={{ marginRight: '5px' }} />
            Search
          </button>
        </div>
      </div>
    </div>
  );
};

export default SearchPage;
