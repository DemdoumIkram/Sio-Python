from flask import Flask, render_template, request
from PyPDF2 import PdfReader

app = Flask(__name__)

documents = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/documents", methods=["POST"])
def upload_pdf():
    file = request.files["file"]

    if not file:
        return "Error readingthe file"

    if file.filename.split(".")[1] != "pdf":
        return "Not a PDF"

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    document_id = len(documents)
    documents[document_id] = {
        "text": text,
        "meta": reader.metadata
    }
    return document_status(document_id)

@app.route("/documents/<int:id>", methods=["GET"])
def document_status(id):
    if id not in documents:
        return {"error": "document not found"}, 404
    meta = documents[id]["meta"]
    pdf_metadata = {
        'title': meta["/Title"],
        'author': meta["/Author"],
        'subject': meta["/Subject"],
        'keywords': meta["/Keywords"],
        'producer': meta["/Producer"],
        'creationDate': meta["/CreationDate"],
        'text': documents[id]["text"]
    }
    return render_template("metadata.html", pdf_metadata=pdf_metadata)