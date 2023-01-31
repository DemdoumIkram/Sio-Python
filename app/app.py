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
    return documents[document_id]