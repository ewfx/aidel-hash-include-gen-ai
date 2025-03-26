import React, { useState } from 'react';
import './App.css';
import { FaSearch } from 'react-icons/fa';

const App = () => {
  const [fileUploaded, setFileUploaded] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');

  const transactions = [
      { id: 1000000001, payer: "TechCorp Ltd", receiver: "FinanceHub Inc", transactionDetails: "Purchase", amount: "$10M", country: "USA", riskScore: 90, confidenceScore: 95 },
      { id: 1000000002, payer: "GlobalBank PLC", receiver: "RetailTrade LLC", transactionDetails: "Transfer", amount: "$20M", country: "UK", riskScore: 70, confidenceScore: 85 },
      { id: 1000000003, payer: "GreenEnergy Co.", receiver: "EcoFinance Ltd", transactionDetails: "Refund", amount: "$5M", country: "Canada", riskScore: 60, confidenceScore: 80 },
      { id: 1000000004, payer: "HealthMed Corp", receiver: "WellnessTech Inc", transactionDetails: "Payment", amount: "$50M", country: "USA", riskScore: 95, confidenceScore: 90 },
      { id: 1000000005, payer: "AutoMotive Group", receiver: "SpeedyParts LLC", transactionDetails: "Purchase", amount: "$30M", country: "Australia", riskScore: 40, confidenceScore: 70 },
      { id: 1000000006, payer: "FoodSupply Ltd", receiver: "FreshFarm Inc", transactionDetails: "Donation", amount: "$15M", country: "Germany", riskScore: 80, confidenceScore: 88 },
      { id: 1000000007, payer: "LuxuryHomes Ltd", receiver: "RealEstatePro LLC", transactionDetails: "Transfer", amount: "$25M", country: "Spain", riskScore: 45, confidenceScore: 75 },
      { id: 1000000008, payer: "CyberSecure Ltd", receiver: "DataProtect Inc", transactionDetails: "Payment", amount: "$100M", country: "USA", riskScore: 85, confidenceScore: 92 },
      { id: 1000000009, payer: "SmartTech Solutions", receiver: "InnoGadgets Ltd", transactionDetails: "Refund", amount: "$15M", country: "Canada", riskScore: 60, confidenceScore: 80 },
      { id: 1000000010, payer: "CloudNet Corp", receiver: "ITServices PLC", transactionDetails: "Transfer", amount: "$70M", country: "UK", riskScore: 50, confidenceScore: 78 },
 
    
  ];

  const handleFileUpload = () => {
    setFileUploaded(true);
  };

  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const filteredTransactions = transactions.filter(
    (transaction) =>
      transaction.id.toString().includes(searchTerm) ||
      transaction.payer.toLowerCase().includes(searchTerm.toLowerCase()) ||
      transaction.receiver.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="App">
      <div className="navbar">
        <div className="app-name">Risk Analysis</div>
        <div className="navbar-links">
          <a href="#">Home</a>
          <a href="#">About</a>
          <a href="#">Contact</a>
        </div>
      </div>

      <div className="file-upload-box">
  <label htmlFor="file-upload">Upload File</label>
  <input id="file-upload" type="file" onChange={handleFileUpload} />
</div>

      {fileUploaded && (
        <div>
<div className="search-container">
  <FaSearch className="search-icon" />
  <input
    className="search-input"
    type="text"
    placeholder="Search by ID, Payer or Receiver"
    value={searchTerm}
    onChange={handleSearchChange}
  />
</div>
          <div className="data-table">
            <table>
            <thead>
  <tr>
    <th>Transaction ID</th>
    <th>Payer</th>
    <th>Receiver</th>
    <th>Transaction Details</th>
    <th>Amount</th>
    <th>Country</th>
    <th>Risk Score</th>  {/* Ensure this column is correctly defined */}
    <th>Confidence Score</th>  {/* This must be separate */}
    <th>Actions</th>
  </tr>
</thead>
<tbody>
  {filteredTransactions.map((transaction) => (
    <tr key={transaction.id}>
      <td>{transaction.id}</td>
      <td>{transaction.payer}</td>
      <td>{transaction.receiver}</td>
      <td>{transaction.transactionDetails}</td>
      <td>{transaction.amount}</td>
      <td>{transaction.country}</td>

            {/* Risk Score with Text Color */}
            <td className={`risk-score ${
                transaction.riskScore > 80
                  ? "text-red"
                  : transaction.riskScore > 50
                  ? "text-yellow"
                  : "text-green"
              }`}>
                {transaction.riskScore}
              </td>

              {/* Confidence Score with Text Color */}
              <td className={`confidence-score ${
                transaction.confidenceScore > 80
                  ? "text-green"
                  : transaction.confidenceScore > 50
                  ? "text-yellow"
                  : "text-red"
              }`}>
                {transaction.confidenceScore}
              </td>
      {/* Action Buttons */}
      <td>
        <button className="summary">Summary</button>
        <button className="report">Report</button>
        <button className="download">Download</button>
        
      </td>
    </tr>
  ))}
</tbody>



            </table>
          </div>
        </div>
      )}

      <div className="footer">
        <p>
          <a href="#">Disclaimer</a> | <a href="#">Terms of Service</a> |{' '}
          <a href="#">Privacy Policy</a>
        </p>
      </div>
    </div>
  );
};

export default App;
