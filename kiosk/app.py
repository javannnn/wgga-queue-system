from flask import Flask, render_template, request
import random
import datetime
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Set up rotating file logger
handler = RotatingFileHandler("kiosk.log", maxBytes=1_000_000, backupCount=1)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
handler.setFormatter(formatter)
app.logger.addHandler(handler)

@app.route("/")
def kiosk():
    return render_template("kiosk.html")

@app.route("/ticket", methods=["POST"])
def generate_ticket():
    ticket_type = request.form["type"]
    ticket_number = f"{ticket_type.upper()}-{random.randint(100,999)}"
    issued_at = datetime.datetime.now().strftime("%H:%M:%S")
    app.logger.info("Ticket issued %s (%s) at %s", ticket_number, ticket_type, issued_at)
    # TODO: integrate with printer hardware here
    return render_template("ticket.html", ticket_number=ticket_number, issued_at=issued_at, ticket_type=ticket_type)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True)
