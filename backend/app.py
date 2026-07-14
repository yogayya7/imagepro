from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {
        "project": "ImagePro",
        "status": "Running",
        "version": "1.0"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)