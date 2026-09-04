\# Moodle Deadline Tracker



A small automated tool that reads my SDU Moodle deadlines and sends me a Telegram

reminder every morning — so I stop missing assignments I never noticed in Moodle.



\## How it works



1\. Moodle publishes a personal calendar feed (a dynamic `.ics` URL tied to my account).

2\. A Python script (`tracker.py`) fetches that feed, parses it with the `icalendar`

&#x20;  library, and calculates a countdown ("2d 5h") for each upcoming deadline.

3\. It sends the formatted list to a personal Telegram bot via the Telegram Bot API.

4\. A GitHub Actions workflow runs this script automatically every day at 5:30 AM

&#x20;  (Almaty time) — entirely in the cloud, so it works even if my laptop is off.

5\. The same workflow can also be triggered manually anytime for an on-demand check.



\## Stack



\- Python (`requests`, `icalendar`, `python-dotenv`)

\- Telegram Bot API

\- GitHub Actions (scheduled + manual cron jobs, secrets management)



\## Setup



Requires three environment variables (set as GitHub Secrets, or in a local `.env`

for testing): `MOODLE\_CALENDAR\_URL`, `TELEGRAM\_BOT\_TOKEN`, `TELEGRAM\_CHAT\_ID`.



\## Possible next steps



\- Track which deadlines are already submitted vs. still pending

\- Support multiple courses/calendars at once

