# config.py

RTSP_URL = "rtsp://admin:Adminpmpl@12345@192.168.32.93:554/Streaming/Channels/101"

DB_CONFIG = {
    "host": "192.168.32.88",
    "user": "workshop_user",
    "password": "Workshop@123",
    "database": "prem_motors",
    "port": 3306,
    "auth_plugin": "mysql_native_password"
}

FRAME_SKIP = 5
EVENT_COOLDOWN = 300  # seconds

SHOW_GUI = False   # server running
# SHOW_GUI = True  # local running 
