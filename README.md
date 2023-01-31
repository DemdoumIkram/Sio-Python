# PDF Storage & Text extraction

## Project structure
    .
    ├── static                  #Basic styles
    │   └── css
    │      └── main.css
    │   └── samples             #Test Samples
    │       ├── samples.pdf
    │       └── samples.txt
    │
    └── templates               #HTML templates
    │   ├── index.html
    │   ├── metadata.html
    │   └── text.html
    │
    ├── app.py                  #App entrypoint 
    └── unitTest.py                   #UnitTests

## Requirements

- Inside the requirements.txt file with the version dependencies

## API Contract

    Endpoint: /
    Method: GET
    Description: Returns the index page of the application
    Response: An HTML page that serves as the frontend for the application
    Upload PDF Document:

    Endpoint: /documents
    Method: POST
    Description: Uploads a PDF document and stores its metadata and text content
    Request Body: A file object representing the PDF document
    Response: An HTML page displaying the metadata for the uploaded document
    Document Metadata:

    Endpoint: /documents/int:id
    Method: GET
    Description: Retrieves the metadata for a given document ID
    Response: An HTML page displaying the metadata for the document
    Document Text Content:

    Endpoint: /text/int:pdf_id
    Method: GET
    Description: Retrieves the text content for a given document ID
    Response: An HTML page displaying the text content for the document.

## Installation & Running

After unzipping the folder or cloning the repository

$ pip install -r requirements.txt
$ flask run

## Stack

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Pytest](https://docs.pytest.org/en/7.2.x/)

## Author

- Ikram DEMDOUM - SIO CentraleSupélec ikram.demdoum@student-cs.fr