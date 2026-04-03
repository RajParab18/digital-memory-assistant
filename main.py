import streamlit as st
from datetime import datetime
from memory_engine import categorize_note, suggest_action
from storage import save_note, get_notes
from reminder import get_due_reminders
from planner import generate_study_plan
from notifier import should_notify

st.set_page_config(page_title="AI Memory Assistant", layout="wide")

st.title("🧠 AI Digital Memory Assistant")

# INPUT
note = st.text_area("Write your note:")

date = st.date_input("Reminder date")
time = st.time_input("Reminder time")

if st.button("Save Note"):

    category = categorize_note(note)
    suggestion = suggest_action(category)

    reminder = datetime.combine(date, time).strftime("%Y-%m-%d %H:%M")

    save_note(note, category, reminder)

    st.success("Saved!")

    st.info(f"Category: {category}")
    st.info(f"Suggestion: {suggestion}")

    # Study plan
    if category == "Study":
        st.subheader("📚 Study Plan")
        plan = generate_study_plan(reminder)
        for p in plan:
            st.write("- " + p)

# LOAD NOTES
notes = get_notes()

# 📅 CALENDAR VIEW (simple)
st.subheader("📅 Calendar View")

calendar = {}

for n in notes:
    if n["reminder"]:
        date = n["reminder"].split(" ")[0]
        if date not in calendar:
            calendar[date] = []
        calendar[date].append(n["note"])

for d, items in calendar.items():
    st.write(f"### {d}")
    for i in items:
        st.write("- " + i)

# ⏰ REMINDERS
st.subheader("⏰ Active Reminders")

due = get_due_reminders(notes)

for n in due:
    st.warning(f"Reminder: {n['note']}")

# 🔔 NOTIFICATIONS
st.subheader("🔔 Notifications")

for n in notes:
    if n["reminder"]:
        if should_notify(n["reminder"]):
            st.error(f"⏰ Time to work on: {n['note']}")

# 📒 ALL NOTES
st.subheader("📒 All Notes")

for n in notes:
    st.write(f"- {n['note']} ({n['category']})")