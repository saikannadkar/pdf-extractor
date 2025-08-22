
from flask import Flask, request, jsonify
import io
import PyPDF2

app = Flask(__name__)

@app.route("/extract-text", methods=["POST"])
def extract_text():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files["file"]
    reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return jsonify({"text": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
