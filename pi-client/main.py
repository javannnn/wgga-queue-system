from flask import Flask, render_template
import requests

app = Flask(__name__)

BACKEND_API_URL = "http://192.168.1.100:5000/api/queue"  # Change to backend server's LAN/static IP

@app.route("/")
def display_queue():
    try:
        resp = requests.get(BACKEND_API_URL, timeout=2)
        queue = resp.json()
    except Exception:
        queue = []
    return render_template("queue.html", queue=queue)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
