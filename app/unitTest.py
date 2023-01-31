import unittest

from app import app


class TestFlaskApp(unittest.TestCase):
    def test_upload_pdf(self):
        with app.test_client() as c:
            # Test with a valid file
            file = open("static/samples/sample.pdf", "rb")
            response = c.post("/documents", data={"file": file})
            self.assertEqual(response.status_code, 200)

            # Test with a file that is not a PDF
            file = open("static/samples/sample.txt", "rb")
            response = c.post("/documents", data={"file": file})
            self.assertEqual(response.status_code, 400)

    def test_document_status(self):
        with app.test_client() as c:
            # Test with a valid document ID
            file = open("static/samples/sample.pdf", "rb")
            response = c.post("/documents", data={"file": file})
            response = c.get("/documents/0")
            self.assertEqual(response.status_code, 200)

            # Test with an invalid document ID
            response = c.get("/documents/1")
            self.assertEqual(response.status_code, 404)

    def test_get_text_by_id(self):
        with app.test_client() as c:
            # Test with a valid document ID
            response = c.get("/text/0")
            self.assertEqual(response.status_code, 200)

            # Test with an invalid document ID
            response = c.get("/text/1")
            self.assertEqual(response.status_code, 404)
