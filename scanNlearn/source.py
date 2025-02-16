import qrcode
import random
import sqlite3
import os


connection = sqlite3.connect('linkdb.db')
cursor = connection.cursor()

cursor.execute('SELECT allurls from alllinks ORDER BY RANDOM() LIMIT 1')

randval = cursor.fetchone()[0]

connection.close()

# Creates the QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Adds data to the QR code
data = randval
qr.add_data(data)
qr.make(fit=True)

# Creates an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Saves image to my img folder

project_root = os.path.dirname(os.path.abspath(__file__))

# Build path to QR code directory
folder_path = os.path.join(project_root, 'include,')

file_name = "qrcode.png"
img_path = f"{folder_path}/{file_name}"

img.save(img_path)
print(f"QR code saved to: {img_path}")



