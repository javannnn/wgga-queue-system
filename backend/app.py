from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import logging
from logging.handlers import RotatingFileHandler
import os
import requests

load_dotenv()

app = Flask(__name__)

# basic rotating file logger
handler = RotatingFileHandler("backend.log", maxBytes=1000000, backupCount=1)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
handler.setFormatter(formatter)
app.logger.addHandler(handler)

GIZE_URL = os.getenv("GIZE_API_URL", "http://192.168.1.6/api/resource/Patient Appointment")
AUTH = (
    os.getenv("GIZE_AUTH_USER", "8887ac7f9febb43"),
    os.getenv("GIZE_AUTH_PASS", "a4390d53c380bba"),
)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/queue")
def get_queue():
    try:
        resp = requests.get(GIZE_URL, auth=AUTH, timeout=5)
        data = resp.json()
        return jsonify(data.get("data", []))
    except Exception as exc:
        app.logger.warning("Falling back to sample data: %s", exc)
        return jsonify([
            {
                "name": "HLC-APP-2025-36943",
                "patient_name": "LEMELEM MENGISTU",
                "appointment_time_12": "2:16 PM",
                "status": "Closed",
                "practitioner_name": "Destaw Mulie",
                "department": "OPD",
            },
            {
                "name": "HLC-APP-2025-36942",
                "patient_name": "JOHN DOE",
                "appointment_time_12": "2:30 PM",
                "status": "Open",
                "practitioner_name": "Dr. Example",
                "department": "OPD",
            },
        ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
