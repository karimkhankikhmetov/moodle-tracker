import os
import requests
from icalendar import Calendar
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("MOODLE_CALENDAR_URL")

response = requests.get(url)
response.raise_for_status()

calendar = Calendar.from_ical(response.text)

for component in calendar.walk():
    if component.name == "VEVENT":
        summary = component.get("summary")
        start = component.get("dtstart").dt
        print(f"{summary} — {start}")

print("Done.")