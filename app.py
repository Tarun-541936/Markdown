from flask import Flask, jsonify, request
import time
import requests

app = Flask(__name__)

start_time = time.time()
checks = []

@app.route("/")
def home():
    return jsonify(message="Welcome to Health API")

@app.route("/health")
def health():
    uptime = time.time() - start_time
    return jsonify(status="ok", uptime=uptime)

@app.route("/check")
def check():
    url = request.args.get("url")
    try:
        start = time.time()
        r = requests.get(url)
        duration = time.time() - start

        result = {
            "url": url,
            "status_code": r.status_code,
            "response_time": duration
        }

        checks.append(result)
        return jsonify(result)

    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route("/report")
def report():
    return jsonify(last_10_checks=checks[-10:])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)