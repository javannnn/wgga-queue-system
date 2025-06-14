from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/queue")
def get_queue():
    # TODO: Replace with Gize API logic
    return jsonify([])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
