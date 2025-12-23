# ocr_module.py
import cv2
import re
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="en", use_doc_unwarping=False)

NORMAL_PLATE = re.compile(r"^[A-Z]{2}\d{1,2}[A-Z]{1,2}\d{4}$")
BH_PLATE = re.compile(r"^\d{2}BH\d{4}[A-Z]{2}$")

def preprocess(img):
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

def extract_plate_text(img):
    results = ocr.predict(img)
    best_text, best_conf = None, 0.0

    for res in results:
        if "rec_text" in res and "rec_score" in res:
            if res["rec_score"] > best_conf:
                best_text = res["rec_text"]
                best_conf = res["rec_score"]

    return best_text, best_conf

def validate_plate(text):
    if not text:
        return False, None

    plate = text.replace(" ", "").upper()
    if BH_PLATE.match(plate):
        return True, "BH"
    if NORMAL_PLATE.match(plate):
        return True, "NORMAL"

    return False, None
