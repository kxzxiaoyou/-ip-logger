from flask import Flask, request, render_template
from datetime import datetime
import smtplib
import os

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{timestamp}] Visitor IP: {user_ip}"
    send_email("sces9204@gmail.com", message)
    return render_template("index.html")

def send_email(to, msg):
    gmail_user = os.environ.get("GMAIL_USER")
    gmail_pass = os.environ.get("GMAIL_PASS")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(gmail_user, gmail_pass)
    server.sendmail(gmail_user, to, msg)
    server.quit()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
