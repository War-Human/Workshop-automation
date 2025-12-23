# main.py
import cv2
import time
import logging
import os

from config import RTSP_URL, FRAME_SKIP, SHOW_GUI
from camera import process_frame

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/workshop.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def main():
    while True:
        try:
            cap = cv2.VideoCapture(RTSP_URL)

            if not cap.isOpened():
                logging.error("RTSP open failed, retrying...")
                time.sleep(5)
                continue

            count = 0
            logging.info("Workshop automation running")

            while True:
                ret, frame = cap.read()
                if not ret:
                    logging.warning("Frame lost, reconnecting")
                    break

                count += 1
                if count % FRAME_SKIP == 0:
                    process_frame(frame)

                if SHOW_GUI:
                    cv2.imshow("Workshop", frame)
                    cv2.waitKey(1)

        except Exception:
            logging.exception("Fatal error")
            time.sleep(5)

if __name__ == "__main__":
    main()
