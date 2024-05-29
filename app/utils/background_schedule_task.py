from datetime import datetime
from datetime import timezone

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger


def daily_task_example():
    print('Daily task executed at', datetime.now(timezone.utc))

# Code to start the background scheduler and schedule the daily task example
def start():
    """
    Starts the background scheduler and schedules a daily task example.

    This function creates a background scheduler and sets a cron trigger to run the
    daily task example. It is important to note that when starting the project with
    multiple workers, this function should only be called once to avoid duplicate
    scheduling of the task.

    Warning:
        When starting the project with multiple workers, ensure that this function is
        only called once to avoid duplicate scheduling of the task.

    """
    scheduler = BackgroundScheduler()
    trigger = CronTrigger(hour=1, minute=0, second=0, timezone='UTC')
    scheduler.add_job(daily_task_example, trigger)
    scheduler.start()