# forwarder.py
# pip install flask requests
from flask import Flask, request
from datetime import datetime, timezone, timedelta
import os
import requests

app = Flask(__name__)
LOGFILE = "events.log"

# === CONFIG - SET THESE ===
TELEGRAM_BOT_TOKEN = "8089785003:AAF4XH3yBBO3pAVtasUMxXfTHXRMBfRxnjo"   # e.g. "123456789:ABCdefGhIJK_lmnopQRstuV"
TELEGRAM_CHAT_ID   = "8212541315"   # chat id (user or group) to receive the message, as string or int
# ==========================

def ist_now_iso():
    now_utc = datetime.utcnow().replace(tzinfo=timezone.utc)
    ist = now_utc + timedelta(hours=5, minutes=30)
    return ist.strftime("%Y-%m-%d %H:%M:%S IST")

def append_line(line):
    with open(LOGFILE, "a") as f:
        f.write(line + "\n")

def send_telegram(text):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram not configured (token/chat_id missing). Skipping send.")
        return None
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "Markdown"}
    try:
        r = requests.post(url, json=payload, timeout=5)
        print("Telegram response:", r.status_code, r.text)
        return r
    except Exception as e:
        print("Telegram send error:", e)
        return None
      @app.route("/notify", methods=["GET"])
def notify():
    value = request.args.get("value", "")
    t = request.args.get("t", "")
    dev = request.args.get("dev", "")
    lat = request.args.get("lat", "")
    lon = request.args.get("lon", "")
    client_ip = request.remote_addr

    ts_ist = ist_now_iso()
    line = f"{ts_ist} | dev={dev} | value={value} | t={t} | lat={lat} | lon={lon} | from={client_ip}"
    print(line)
    append_line(line)

    # build Telegram message
    msg = f"🚨 *ALERT* from `{dev}`\n*Value*: {value}\n*Time (IST)*: {ts_ist}\n"
    if lat and lon:
        msg += f"*Location*: {lat}, {lon}\nhttps://www.google.com/maps/search/?api=1&query={lat},{lon}\n"
    msg += f"_Source IP_: {client_ip}"

    send_telegram(msg)

    return "OK\n", 200

@app.route("/logs", methods=["GET"])
def get_logs():
    if not os.path.exists(LOGFILE):
        return "No log file", 404
    with open(LOGFILE, "r") as f:
        return "<pre>" + f.read() + "</pre>"

if __name__ == "__main__":
    print("Forwarder starting on port 5000")
    print("Logs will be appended to", LOGFILE)
    app.run(host="0.0.0.0", port=5000)
