from datetime import datetime

from flask import Flask, render_template, request
from pypdf import PdfReader

# Initialize the Flask application
app = Flask(__name__)

# Dictionary to store uploaded PDF documents
documents = {}

# Route for the index page
@app.route("/")
def index():
    return render_template("index.html")

# Route to upload PDF documents
@app.route("/documents", methods=["POST"])
def upload_pdf():
    # Get the uploaded file from the request
    file = request.files["file"]

    # Check if the file was successfully read
    if not file:
        return {"error": "Error reading the file"}, 400

    # Check if the uploaded file is a PDF
    if file.filename.split(".")[1] != "pdf":
        return {"error": "document is not a PDF"}, 400

    # Read the PDF using PyPDF library
    reader = PdfReader(file)

    # Extract text from each page of the PDF
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    # Extract metadata from the PDF
    meta = reader.metadata

    # Convert the creation date to a datetime object
    date = datetime.strptime(meta["/CreationDate"][2:], "%Y%m%d%H%M%SZ")

    # Assign an ID to the document and store it in the dictionary
    document_id = len(documents)
    documents[document_id] = {
        "title": meta["/Title"],
        "author": meta["/Author"],
        "subject": meta["/Subject"],
        "keywords": meta["/Keywords"],
        "producer": meta["/Producer"],
        "creationDate": date,
        "content": "http://localhost:5000/text/" + str(document_id),
        "text": text,
        "status": "success",
    }

    # Call the function to display the metadata for the uploaded document
    return document_status(document_id)

# Route to display the metadata for a given document ID
@app.route("/documents/<int:id>", methods=["GET"])
def document_status(id):
    # Check if the document with the given ID exists
    if id not in documents:
        return {"error": "document not found"}, 404
    # Return the metadata for the document
    return render_template("metadata.html", pdf_metadata=documents[id]), 200

# Route to display the text content for a given document ID
@app.route("/text/<int:pdf_id>", methods=["GET"])
def get_text_by_id(pdf_id):
    # Check if the document with the given ID exists
    if pdf_id not in documents:
        return {"error": "document not found"}, 404
    # Return the text content for the document
    return render_template("text.html", text=documents[pdf_id]["text"]), 200
