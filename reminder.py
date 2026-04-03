from datetime import datetime

def get_due_reminders(notes):
    now = datetime.now()
    due = []

    for n in notes:
        if n["reminder"]:
            r = datetime.strptime(n["reminder"], "%Y-%m-%d %H:%M")
            if r <= now:
                due.append(n)

    return due