import json
import os

FILE_NAME = "notes.json"

def load_notes():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_note(note, category, reminder=None):
    notes = load_notes()

    notes.append({
        "note": note,
        "category": category,
        "reminder": reminder
    })

    with open(FILE_NAME, "w") as f:
        json.dump(notes, f, indent=4)

def get_notes():
    return load_notes()