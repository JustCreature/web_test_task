from apscheduler.schedulers.background import BackgroundScheduler
from api.models import Site
from api.services.services import update_statuses

def start():
    scheduler = BackgroundScheduler()

    scheduler.add_job(update_statuses, "interval",
                      seconds=60, id="update_statuses_001",
                      replace_existing=True)
    print("Job added")
    scheduler.start()
