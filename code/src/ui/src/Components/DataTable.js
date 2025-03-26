import React, { useState } from "react";
import "../App.css"; // Import styles

function DataTable({ data, searchTerm }) {
  const [selectedTransaction, setSelectedTransaction] = useState(null);

  // Function to show the transaction summary in a pop-up
  const handleSummary = (transaction) => {
    setSelectedTransaction(transaction);
  };

  // Function to close the summary pop-up
  const closeSummary = () => {
    setSelectedTransaction(null);
  };

  // Function to download the summary details as a text file
  const handleDownload = (transaction) => {
    if (!transaction) return;

    const { id, payer, receiver, riskScore, confidenceScore, country } = transaction;
    const summaryText = `
Transaction ID: ${id}
Extracted Entity: [ ${payer} ], [ ${receiver} ]
Entity Type: [ Opencorporates, Corporation ]
Risk Score: ${riskScore}
Confidence Score: ${confidenceScore}
Supporting Evidence: [ Opencorporates, Company website ]
Reason: ${payer} is not on sanctions list but an entity of interest. It is owned by ${country} businessman and related to ${receiver}, a sanctioned entity.
    `;

    const blob = new Blob([summaryText], { type: "text/plain" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = `Transaction_${id}_Summary.txt`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  // Function to show report success message
  const handleReport = () => {
    alert("Reported successfully");
  };

  // Filtering data based on search term
  const filteredData = data.filter(
    (transaction) =>
      transaction.id.toString().includes(searchTerm) ||
      transaction.payer.toLowerCase().includes(searchTerm.toLowerCase()) ||
      transaction.receiver.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
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
            <th>Risk Score</th>
            <th>Confidence Score</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {filteredData.map((transaction) => (
            <tr key={transaction.id}>
              <td>{transaction.id}</td>
              <td>{transaction.payer}</td>
              <td>{transaction.receiver}</td>
              <td>{transaction.transactionDetails}</td>
              <td>{transaction.amount}</td>
              <td>{transaction.country}</td>

              {/* Risk Score with Text Color */}
              <td
                className={`risk-score ${
                  transaction.riskScore > 0.80
                    ? "text-red"
                    : transaction.riskScore > 0.50
                    ? "text-orange"
                    : "text-green"
                }`}
              >
                {transaction.riskScore}
              </td>

              {/* Confidence Score with Text Color */}
              <td
                className={`confidence-score ${
                  transaction.confidenceScore > 0.80
                    ? "text-green"
                    : transaction.confidenceScore > 0.50
                    ? "text-orange"
                    : "text-red"
                }`}
              >
                {transaction.confidenceScore}
              </td>

              <td>
                <button className="summary" onClick={() => handleSummary(transaction)}>Summary</button>
                <button className="report" onClick={handleReport}>Report</button>
                <button className="download" onClick={() => handleDownload(transaction)}>Download</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Pop-up summary modal */}
      {selectedTransaction && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h2>Transaction Summary</h2>
            <p><strong>Transaction ID:</strong> {selectedTransaction.id}</p>
            <p><strong>Extracted Entity:</strong> [ {selectedTransaction.payer} ], [ {selectedTransaction.receiver} ]</p>
            <p><strong>Entity Type:</strong> [ Opencorporates, Corporation ]</p>
            <p><strong>Risk Score:</strong> {selectedTransaction.riskScore}</p>
            <p><strong>Confidence Score:</strong> {selectedTransaction.confidenceScore}</p>
            <p><strong>Supporting Evidence:</strong> [ Opencorporates, Company website ]</p>
            <p><strong>Reason:</strong> {selectedTransaction.payer} is not on sanctions list but an entity of interest. It is owned by {selectedTransaction.country} businessman and related to {selectedTransaction.receiver}, a sanctioned entity.</p>
            
            <button className="download-button" onClick={() => handleDownload(selectedTransaction)}>Download</button>
            <button className="close-button" onClick={closeSummary}>Close</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default DataTable;
