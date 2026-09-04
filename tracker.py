import os
import requests
from datetime import datetime, timezone
from icalendar import Calendar
from dotenv import load_dotenv

load_dotenv()

calendar_url = os.getenv("MOODLE_CALENDAR_URL")
token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

response = requests.get(calendar_url)
response.raise_for_status()
calendar = Calendar.from_ical(response.text)

now = datetime.now(timezone.utc)
lines = []

for component in calendar.walk():
    if component.name == "VEVENT":
        summary = str(component.get("summary"))
        start = component.get("dtstart").dt
        if start.tzinfo is None:
            start = start.replace(tzinfo=timezone.utc)
        delta = start - now
        if delta.total_seconds() > 0:
            days = delta.days
            hours = delta.seconds // 3600
            lines.append(f"{summary} — due in {days}d {hours}h")

message = "Today:\n" + "\n".join(lines) if lines else "No upcoming deadlines found."

url = f"https://api.telegram.org/bot{token}/sendMessage"
requests.post(url, data={"chat_id": chat_id, "text": message})
print("Sent:", message)