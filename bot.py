import os
import time
import subprocess
import schedule

SIGNAL_CLI = "signal-cli"
PHONE = os.environ.get("PHONE")
GROUPS = os.environ.get("GROUP_IDS", "").split(",")
MESSAGE = os.environ.get("POST_TEXT")
INTERVAL_HOURS = int(os.environ.get("INTERVAL_HOURS", "3"))

def post_to_groups():
    for group in GROUPS:
        try:
            subprocess.run([
                SIGNAL_CLI, "-u", PHONE,
                "send", "-g", group.strip(),
                "-m", MESSAGE
            ], check=True)
            print(f"Gepostet in Gruppe {group}")
        except Exception as e:
            print(f"Fehler in Gruppe {group}: {e}")

schedule.every(INTERVAL_HOURS).hours.do(post_to_groups)

print("Bot gestartet!")
post_to_groups()

while True:
    schedule.run_pending()
    time.sleep(60)
