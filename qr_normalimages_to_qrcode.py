import qrcode
from PIL import Image
import os

def compress_image(image_path):
    image = Image.open(image_path)
    filename, file_extension = os.path.splitext(image_path)
    compressed_image_path = f"{filename}_compressed{file_extension}"
    image.save(compressed_image_path, optimize=True, quality=50)
    return compressed_image_path

def image_to_qrcode(image_path):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add the image URL to the QR code
    qr.add_data(f"file://{image_path}")

    # Compile the QR code data
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image to a file
    img.save("qrcode.png")

# Example usage:
image_path = "/home/rajashekar/Pictures/mac.png"
compressed_image_path = compress_image(image_path)
image_to_qrcode(compressed_image_path)