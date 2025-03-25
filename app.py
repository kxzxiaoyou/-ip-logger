from flask import Flask, request, render_template
from datetime import datetime
import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header

app = Flask(__name__)

@app.route('/')
def index():
    # 擷取 IP
    user_ip = request.headers.get('X-Forwarded-For')
    if user_ip:
        user_ip = user_ip.split(',')[0].strip()
    else:
        user_ip = request.remote_addr

    # 擷取 User-Agent
    user_agent = request.headers.get('User-Agent')

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{timestamp}]\nVisitor IP: {user_ip}\nUser Agent: {user_agent}"
    send_email("sces9204@gmail.com", message)
    return render_template("index.html")

def send_email(to, msg):
    gmail_user = os.environ.get("GMAIL_USER")
    gmail_pass = os.environ.get("GMAIL_PASS")

    mime_msg = MIMEText(msg, _charset='utf-8')
    mime_msg['Subject'] = Header('Visitor IP Log', 'utf-8')
    mime_msg['From'] = gmail_user
    mime_msg['To'] = to

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(gmail_user, gmail_pass)
    server.sendmail(gmail_user, [to], mime_msg.as_string())
    server.quit()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
