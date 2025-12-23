# camera.py
from ocr_module import preprocess, extract_plate_text, validate_plate
from vehicle_logic import handle_entry, handle_exit

def process_frame(frame):
    roi = frame[88:690, 361:1250]
    processed = preprocess(roi)

    text, conf = extract_plate_text(processed)
    if conf < 0.6:
        return

    valid, plate_type = validate_plate(text)
    if not valid:
        return

    plate = text.replace(" ", "").upper()

    from vehicle_logic import vehicle_state
    if plate not in vehicle_state:
        handle_entry(plate, plate_type)
    else:
        handle_exit(plate)
