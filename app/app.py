from flask import Flask, render_template, request
from PyPDF2 import PdfReader

app = Flask(__name__)

documents = {}


@app.route("/")
def index():
    return render_template("index.html")


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

    meta = reader.metadata

    document_id = len(documents)
    documents[document_id] = {
        "title": meta["/Title"],
        "author": meta["/Author"],
        "subject": meta["/Subject"],
        "keywords": meta["/Keywords"],
        "producer": meta["/Producer"],
        "creationDate": meta["/CreationDate"],
        "text": text,
    }
    return document_status(document_id)


@app.route("/documents/<int:id>", methods=["GET"])
def document_status(id):
    if id not in documents:
        return {"error": "document not found"}, 404
    return render_template("metadata.html", pdf_metadata=documents[id])


@app.route("/text/<int:pdf_id>", methods=["GET"])
def get_text_by_id(pdf_id):
    if pdf_id not in documents:
        return {"error": "document not found"}, 404
    return render_template("text.html", text=documents[pdf_id]["text"]), 200
