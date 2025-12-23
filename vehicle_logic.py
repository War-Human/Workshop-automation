# vehicle_logic.py
from datetime import datetime
from config import EVENT_COOLDOWN
from database import insert_entry, update_exit

vehicle_state = {}

def handle_entry(plate, plate_type):
    now = datetime.now()
    if plate not in vehicle_state:
        vehicle_state[plate] = {
            "entry_time": now,
            "last_seen": now
        }
        insert_entry(plate, plate_type)

def handle_exit(plate):
    now = datetime.now()
    last_seen = vehicle_state[plate]["last_seen"]

    if (now - last_seen).total_seconds() < EVENT_COOLDOWN:
        vehicle_state[plate]["last_seen"] = now
        return

    entry_time = vehicle_state[plate]["entry_time"]
    duration = int((now - entry_time).total_seconds() / 60)
    update_exit(plate, duration)
    del vehicle_state[plate]
