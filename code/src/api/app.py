from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from transaction_parser import parse_transaction_file

load_dotenv()

app = Flask(__name__)

SEC_API_KEY = os.getenv('SEC_API_KEY')
SERP_API_KEY = os.getenv('SERP_API_KEY')


@app.route("/api/analyze_transactions", methods=["POST"])
def analyze_transactions():
    if "file" not in request.files:
        return jsonify({"error": "No file part provided"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    file_path = f"/transaction_files/{file.filename}"
    file.save(file_path)

    # Extract the entity information out of the file
    transaction_df, file_type = parse_transaction_file(file_path)

    for index, transaction in transaction_df.iterrows():
        if file_type == "semistrcutured":
            sender = transaction['Sender Name']
            receiver = transaction['Receiver Name']
            transaction_notes = transaction['Additional Notes']
