
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

MESSAGE = os.environ.get("APP_MESSAGE", "Hello from tf-mini-3tier!")

@app.get("/")
def index():
    return f"<h1>tf-mini-3tier</h1><p>{MESSAGE}</p>"

@app.get("/health")
def health():
    return jsonify(status="ok", message=MESSAGE), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
