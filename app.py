from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "ArgoCD GitOps Demo - Version 2. Argocd is being tested.",
        "environment": os.getenv("ENVIRONMENT", "dev")
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
