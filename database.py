# database.py
import mysql.connector
from datetime import datetime
from config import DB_CONFIG

db = mysql.connector.connect(**DB_CONFIG)
cursor = db.cursor()

def ensure_connection():
    if not db.is_connected():
        db.reconnect(attempts=3, delay=5)

def insert_entry(plate, plate_type):
    ensure_connection()
    cursor.execute("""
        INSERT INTO vehicle_logs (plate_number, plate_type, entry_time)
        VALUES (%s, %s, %s)
    """, (plate, plate_type, datetime.now()))
    db.commit()

def update_exit(plate, duration):
    ensure_connection()
    cursor.execute("""
        UPDATE vehicle_logs
        SET exit_time=%s, total_minutes=%s
        WHERE plate_number=%s AND exit_time IS NULL
    """, (datetime.now(), duration, plate))
    db.commit()
