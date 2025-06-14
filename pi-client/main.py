from flask import Flask, render_template
import requests
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

handler = RotatingFileHandler("pi_client.log", maxBytes=1000000, backupCount=1)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
handler.setFormatter(formatter)
app.logger.addHandler(handler)

BACKEND_API_URL = "http://192.168.1.100:5000/api/queue"  # Change to backend server's LAN/static IP

@app.route("/")
def display_queue():
    error = False
    try:
        resp = requests.get(BACKEND_API_URL, timeout=2)
        queue = resp.json()
    except Exception as exc:
        app.logger.warning("Backend unreachable: %s", exc)
        queue = []
        error = True
    return render_template("queue.html", queue=queue, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
