import qrcode
from PIL import Image

data = {
    "name": "Rajasekhar Reddy",
    "email": "rajasekharreddy@gmail.com",
    "phone": "1234567890"
}

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data(str(data))
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img = img.resize((200, 200))
img.save("qr_code.png")



############################################ FOR MORE THAN 1 DATA #####################################
# import qrcode
# from PIL import Image
#
# contacts = [
#     {
#         "name": "Rajasekhar Reddy",
#         "email": "rajasekharreddy@gmail.com",
#         "phone": "1234567890"
#     },
#     {
#         "name": "Chandrasekhar Reddy",
#         "email": "chandrasekharreddy@gmail.com",
#         "phone": "1234567890"
#     }
# ]
#
# for contact in contacts:
#     data = str(contact)  # Convert contact dict to string
#
#     qr = qrcode.QRCode(
#         version=1,  # Adjust version for larger data
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4
#     )
#     qr.add_data(data)
#     qr.make(fit=True)
#
#     img = qr.make_image(fill_color="black", back_color="white")
#     img = img.resize((200, 200))
#
#     # Generate unique file names to avoid overwriting
#     file_name = f"qr_code_{contact['name']}.png"
#     img.save(file_name)
#     print(f"QR code for {contact['name']} saved as {file_name}")