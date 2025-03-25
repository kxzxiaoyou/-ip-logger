from flask import Flask, request, render_template
from datetime import datetime
import smtplib
import os
import requests
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

    # 擷取 User-Agent / 語言
    user_agent = request.headers.get('User-Agent')
    accept_language = request.headers.get('Accept-Language', 'Unknown')

    # 用 IP 查詢地理位置
    location_info = "Unknown"
    map_link = ""
    try:
        res = requests.get(f"https://ipapi.co/{user_ip}/json/")
        data = res.json()
        country = data.get("country_name", "N/A")
        region = data.get("region", "N/A")
        city = data.get("city", "N/A")
        org = data.get("org", "N/A")
        lat = data.get("latitude", "")
        lon = data.get("longitude", "")
        location_info = f"{country}, {region}, {city} ({org})"
        if lat and lon:
            map_link = f"https://www.google.com/maps?q={lat},{lon}"
    except Exception as e:
        location_info = f"Error retrieving location: {e}"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = f"""[IP Access Log]

Time: {timestamp}
IP Address: {user_ip}
Location: {location_info}
Map: {map_link}
Browser Info: {user_agent}
Language: {accept_language}
"""

    send_email("sces9204@gmail.com", message)
    return render_template("index.html")

def send_email(to, msg):
    gmail_user = os.environ.get("GMAIL_USER")
    gmail_pass = os.environ.get("GMAIL_PASS")

    mime_msg = MIMEText(msg, _charset='utf-8')
    mime_msg['Subject'] = Header('📡 Visitor IP Tracking Log', 'utf-8')
    mime_msg['From'] = gmail_user
    mime_msg['To'] = to

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(gmail_user, gmail_pass)
    server.sendmail(gmail_user, [to], mime_msg.as_string())
    server.quit()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
