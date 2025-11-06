import requests
import time

# Replace with your actual Discord webhook URL
WEBHOOK_URL = "https://discordapp.com/api/webhooks/1435906466136719481/edRl9gdBwX_YS40gDC3VOu3u0n8TJ_doUx03Wnv1ivki3OpxTuAI5h4dqkwJ-_gHkUd9"

# Your formatted message
MESSAGE = """
@everyone 🚨🚨🚨🚨🚨🚨🚨

**⚠️ ATTENTION TEAM ⚠️**

> **THE NEXT MIKHANYI CONTINUANCE REQUEST**
> **FOR FERI NUMBER:** `2025AUCNA1577575`
> **MUST BE DONE ON:** 🧾 **004** and **005**
> *(as stated in the Excel sheet)*

🚨🚨🚨🚨🚨🚨🚨
"""

# Interval (10 minutes = 600 seconds)
INTERVAL = 1200

def send_message():
    data = {"content": MESSAGE}
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("✅ Message sent successfully.")
    else:
        print(f"⚠️ Failed to send message: {response.status_code} - {response.text}")

if __name__ == "__main__":
    print("🚀 Starting Discord recurring message bot...")
    while True:
        send_message()
        time.sleep(INTERVAL)
