import React, { useState } from 'react';
import { FaSearch } from 'react-icons/fa';

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
    <div style={{ backgroundColor: '#ffffff', minHeight: '100vh', padding: '20px' }}>
      <h1 style={{ textAlign: 'left', marginBottom: '8px', marginLeft: '8px', fontSize: '48px' }}>Famous Quotes</h1>
      <div style={{ display: 'flex', justifyContent: 'center' }}>
        <div style={{ width: '100%', maxWidth: '600px', display: 'flex', alignItems: 'center' }}>
          <input
            type="text"
            placeholder="Search..."
            value={searchTerm}
            onChange={handleSearchInputChange}
            style={{ flex: '1', padding: '10px', fontSize: '16px', border: '1px solid #ccc', borderRadius: '5px 0 0 5px' }}
          />
          <button
            onClick={handleSearchSubmit}
            style={{ padding: '10px 20px', fontSize: '16px', backgroundColor: '#007bff', color: '#ffffff', border: '1px solid #007bff', borderRadius: '0 5px 5px 0', cursor: 'pointer' }}
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
