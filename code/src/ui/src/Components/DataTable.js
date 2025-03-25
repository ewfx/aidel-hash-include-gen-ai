// import React from 'react';

// function DataTable({ data, searchTerm }) {
//   const filteredData = data.filter(
//     (row) =>
//       row.transactionId.toLowerCase().includes(searchTerm.toLowerCase()) ||
//       row.payer.toLowerCase().includes(searchTerm.toLowerCase()) ||
//       row.receiver.toLowerCase().includes(searchTerm.toLowerCase())
//   );

//   return (
//     <div className="data-table">
//       <table>
//         <thead>
//           <tr>
//             <th>Transaction ID</th>
//             <th>Payer</th>
//             <th>Receiver</th>
//             <th>Transaction Details</th>
//             <th>Amount</th>
//             <th>Country</th>
//             <th>Risk Score</th>
//             <th>Confidence Score</th>
//             <th>Actions</th>
//           </tr>
//         </thead>
//         <tbody>
//           {filteredData.map((row, index) => (
//             <tr key={index}>
//               <td>{row.transactionId}</td>
//               <td>{row.payer}</td>
//               <td>{row.receiver}</td>
//               <td>{row.details}</td>
//               <td>{row.amount}</td>
//               <td>{row.country}</td>

//               {/* Risk Score with Proper Alignment */}
//               <td>
//                 <span
//                   className={`risk-score ${
//                     row.riskScore > 80
//                       ? 'high-risk'
//                       : row.riskScore > 50
//                       ? 'medium-risk'
//                       : 'low-risk'
//                   }`}
//                 >
//                   {row.riskScore}
//                 </span>
//               </td>

//               {/* Confidence Score with Proper Alignment */}
//               <td>
//                 <span
//                   className={`confidence-score ${
//                     row.confidenceScore > 80
//                       ? 'high-confidence'
//                       : row.confidenceScore > 50
//                       ? 'medium-confidence'
//                       : 'low-confidence'
//                   }`}
//                 >
//                   {row.confidenceScore}
//                 </span>
//               </td>

//               <td>
//                 <button>Summary</button>
//                 <button className="download">Download</button>
//                 <button className="report">Report</button>
//               </td>
//             </tr>
//           ))}
//         </tbody>
//       </table>
//     </div>
//   );
// }

// export default DataTable;
