import os
import time
import subprocess
import schedule

SIGNAL_CLI = "signal-cli"
SIGNAL_DATA_DIR = "/data"

PHONE = os.environ.get("PHONE")
GROUPS = os.environ.get("GROUP_IDS", "").split(",")
MESSAGE = os.environ.get("POST_TEXT")
INTERVAL_MINUTES = int(os.environ.get("INTERVAL_MINUTES", "10"))


def post_to_groups():
    for group in GROUPS:
        group = group.strip()

        if not group:
            continue

        try:
            subprocess.run(
                [
                    SIGNAL_CLI,
                    "-d",
                    SIGNAL_DATA_DIR,
                    "-u",
                    PHONE,
                    "send",
                    "-g",
                    group,
                    "-m",
                    MESSAGE
                ],
                check=True
            )

            print(f"Gepostet in Gruppe {group}", flush=True)

        except subprocess.CalledProcessError as e:
            print(f"Signal-Fehler in Gruppe {group}: {e}", flush=True)

        except Exception as e:
            print(f"Fehler in Gruppe {group}: {e}", flush=True)


print("Bot gestartet!", flush=True)

post_to_groups()

schedule.every(INTERVAL_MINUTES).minutes.do(post_to_groups)

while True:
    schedule.run_pending()
    time.sleep(60)
