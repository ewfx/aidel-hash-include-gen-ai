import React from "react";
import "../App.css"; // Ensure styles are applied

function Navbar() {
  return (
    <div className="navbar">
      <div className="app-name">Risk Analysis</div>
      <div className="navbar-links">
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Contact</a>
      </div>
    </div>
  );
}

export default Navbar;
