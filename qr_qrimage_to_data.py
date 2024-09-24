import cv2
import pyzbar.pyzbar as pyzbar

def extract_qr_code(image_path):
    """Extracts QR code data from an image.

    Args:
        image_path (str): Path to the image file.

    Returns:
        str: QR code data, or None if no QR code is found.
    """

    # Load the image
    img = cv2.imread(image_path)

    # Detect QR codes in the image
    detected_qrcodes = pyzbar.decode(img)

    # Extract QR code data from the first detected QR code (if any)
    if detected_qrcodes:
        qr_code_data = detected_qrcodes[0].data.decode('utf-8')
        return qr_code_data
    else:
        return None

# Example usage
image_path = "qrcode.png"
qr_code_data = extract_qr_code(image_path)

if qr_code_data:
    print("QR code data:", qr_code_data)
else:
    print("No QR code found in the image.")