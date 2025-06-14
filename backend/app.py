from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)

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
        resp = requests.get(GIZE_URL, auth=AUTH)
        data = resp.json()
        return jsonify(data.get("data", []))
    except Exception:
        # fallback for testing
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
