from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def display_queue():
    return render_template("queue.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
