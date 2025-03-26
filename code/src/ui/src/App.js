import React, { useState } from "react";
import "./App.css";
import Navbar from "./Components/Navbar";
import DataTable from "./Components/DataTable";
import { FaSearch } from "react-icons/fa";

const App = () => {
  const [fileUploaded, setFileUploaded] = useState(false);
  const [searchTerm, setSearchTerm] = useState("");

  const allTransactions = [
    { id: 1000020001, payer: "TechCorp Ltd", receiver: "FinanceHub Inc", transactionDetails: "Purchase", amount: "$10M", country: "USA", riskScore: 0.90, confidenceScore: 0.95 },
    { id: 1004000002, payer: "GlobalBank PLC", receiver: "RetailTrade LLC", transactionDetails: "Transfer", amount: "$20M", country: "UK", riskScore: 0.70, confidenceScore: 0.85 },
    { id: 1000600003, payer: "GreenEnergy Co.", receiver: "EcoFinance Ltd", transactionDetails: "Refund", amount: "$5M", country: "Canada", riskScore: 0.60, confidenceScore: 0.80 },
    { id: 1000500004, payer: "HealthMed Corp", receiver: "WellnessTech Inc", transactionDetails: "Payment", amount: "$50M", country: "USA", riskScore: 0.95, confidenceScore: 0.90 },
    { id: 1100000005, payer: "AutoMotive Group", receiver: "SpeedyParts LLC", transactionDetails: "Purchase", amount: "$30M", country: "Australia", riskScore: 0.40, confidenceScore: 0.70 },
    { id: 1000000006, payer: "FoodSupply Ltd", receiver: "FreshFarm Inc", transactionDetails: "Donation", amount: "$15M", country: "Germany", riskScore: 0.80, confidenceScore: 0.88 },
    { id: 1000006007, payer: "LuxuryHomes Ltd", receiver: "RealEstatePro LLC", transactionDetails: "Transfer", amount: "$25M", country: "Spain", riskScore: 0.45, confidenceScore: 0.75 },
    { id: 1004000008, payer: "CyberSecure Ltd", receiver: "DataProtect Inc", transactionDetails: "Payment", amount: "$100M", country: "USA", riskScore: 0.85, confidenceScore: 0.92 },
    { id: 1000500009, payer: "SmartTech Solutions", receiver: "InnoGadgets Ltd", transactionDetails: "Refund", amount: "$15M", country: "Canada", riskScore: 0.60, confidenceScore: 0.80 },
    { id: 1000070010, payer: "CloudNet Corp", receiver: "ITServices PLC", transactionDetails: "Transfer", amount: "$70M", country: "UK", riskScore: 0.50, confidenceScore: 0.78 },
  ];

  // Show first 5 transactions initially, show all after file upload
  const transactions = fileUploaded ? allTransactions : allTransactions.slice(0, 5);

  const handleFileUpload = (event) => {
    if (event.target.files.length > 0) {
      setFileUploaded(true);
    }
  };

  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
  };

  return (
    <div className="App">
      <Navbar />

      {/* Search Bar and File Upload in a single row */}
      <div className="search-upload-container">
        <div className="search-box">
          <FaSearch className="search-icon" />
          <input
            className="search-input"
            type="text"
            placeholder="Search by ID, Payer or Receiver"
            value={searchTerm}
            onChange={handleSearchChange}
          />
        </div>

        {/* Upload File Button */}
        <button className="upload-button" onClick={() => document.getElementById("fileInput").click()}>
          Upload File
        </button>
        <input type="file" id="fileInput" style={{ display: "none" }} onChange={handleFileUpload} />
      </div>

      <DataTable data={transactions} searchTerm={searchTerm} />

      <div className="footer">
        <p>
          <a href="#">Disclaimer</a> | <a href="#">Terms of Service</a> |{" "}
          <a href="#">Privacy Policy</a>
        </p>
      </div>
    </div>
  );
};

export default App;
