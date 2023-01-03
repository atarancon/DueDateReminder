from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

@scheduler.scheduled_job('cron', day_of_week='mon-sun', hour=12)
def send_reminders():
    # retrieve billing due dates that are coming up
    upcoming_billing_dates = retrieve_upcoming_billing_dates()

    # send reminders to relevant users
    for billing_date in upcoming_billing_dates:
        send_reminder(billing_date.user)

scheduler.start()
