import pytesseract
import cv2
import numpy as np

def process_image(image):
    # Assuming image is passed as a base64-encoded string
    nparr = np.frombuffer(base64.b64decode(image), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # OCR for text extraction
    text = pytesseract.image_to_string(img)

    # Extract metadata (dummy values used for now)
    metadata = {"timestamp": "2024-09-15", "location": "Train 12345"}

    return text, metadata
