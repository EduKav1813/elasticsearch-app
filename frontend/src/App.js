import React, { useState } from "react";
import { FaSearch } from "react-icons/fa";
import "./App.css";

const SearchPage = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const [response, setResponse] = useState(null);

  const handleSearchInputChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleSearchSubmit = async () => {
    console.log("Searching for:", searchTerm);
    const formData = new URLSearchParams();
    formData.append('query', searchTerm);

    try {
      const res = await fetch("http://localhost:5000/", {
        method: 'POST',
        body: formData,
        headers: {
          "Content-Type": 'application/x-www-form-urlencoded',
        },
      });
      const result = await res.json();
      setResponse(result);
      console.log(result)
    } catch (error) {
      console.error("Error:", error);
    }

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
          <button onClick={handleSearchSubmit} className="search-button">
            <FaSearch style={{ marginRight: "5px" }} />
            Search
          </button>
        </div>
      </div>
    </div>
  );
};

export default SearchPage;
