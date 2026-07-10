from flask import Flask
from prometheus_client import Counter, generate_latest
import os, random

app = Flask(__name__)
error_counter = Counter("app_errors_total", "Total API errors")

@app.route("/")
def home():
    fail_mode = os.path.exists("/tmp/fail_mode.flag")
    if fail_mode and random.random() < 0.6:
        error_counter.inc()
        return "API Error!", 500
    return "API OK!"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
