import schedule
import time
import django
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'laborator_django.settings')
django.setup()

from aplicatie1 import tasks

def run_scheduler():
    schedule.every(2).minutes.do(tasks.delete_unconfirmed_users)
    schedule.every().friday.at("16:45").do(tasks.send_newsletter)
    schedule.every(5).minutes.do(tasks.log_system_health)
    schedule.every().monday.at("08:00").do(tasks.generate_weekly_report)
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    try:
        run_scheduler()
    except KeyboardInterrupt:
        print("Scheduler oprit manual.")
        sys.exit()