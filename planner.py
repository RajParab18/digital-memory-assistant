from datetime import datetime

def generate_study_plan(reminder_time):

    now = datetime.now()
    target = datetime.strptime(reminder_time, "%Y-%m-%d %H:%M")

    hours_left = int((target - now).total_seconds() / 3600)

    if hours_left <= 0:
        return ["Time is over. Revise quickly!"]

    plan = []

    for i in range(1, hours_left + 1):
        plan.append(f"Hour {i}: Study + revise key topics")

    return plan