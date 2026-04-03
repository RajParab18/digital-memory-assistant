from datetime import datetime, timedelta

def should_notify(start_time_str):

    start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
    now = datetime.now()

    diff = now - start_time

    hours = diff.total_seconds() / 3600

    # Notify every hour for 3 hours
    if 0 <= hours <= 3:
        if int(hours) == hours:  # every full hour
            return True

    return False