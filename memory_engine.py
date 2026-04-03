def categorize_note(note):
    note = note.lower()

    keywords = {
        "Study": ["exam", "study", "revision", "test"],
        "Work": ["meeting", "project", "deadline"],
        "Personal": ["buy", "shopping", "family"]
    }

    for category, words in keywords.items():
        for w in words:
            if w in note:
                return category

    return "General"


def suggest_action(category):
    return {
        "Study": "Break topic into small parts and revise daily.",
        "Work": "Schedule tasks and set deadlines.",
        "Personal": "Add to your daily to-do list.",
        "General": "Keep note for future reference."
    }.get(category, "No suggestion")