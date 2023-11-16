# Save the image
#img_holder = "example_qrcode.png"
#img.save(img_holder)
#print(f"QR code saved to: {img_holder}")


link1 = "https://www.google.com/search?q=chicken&oq=chicken&gs_lcrp=EgZjaHJvbWUqEAgAEAAYgwEY4wIYsQMYgAQyEAgAEAAYgwEY4wIYsQMYgAQyDQgBEC4YgwEYsQMYgAQyBwgCEAAYgAQyBwgDEC4YgAQyDQgEEAAYgwEYsQMYgAQyDQgFEAAYgwEYsQMYgAQyCggGEAAYsQMYgAQyDQgHEAAYgwEYsQMYgAQyDQgIEAAYgwEYsQMYgAQyDQgJEAAYgwEYsQMYgATSAQgyNDYwajBqN6gCALACAA&sourceid=chrome&ie=UTF-8"
link2 = "https://www.google.com/search?q=cow&oq=cow+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTISCAEQLhgUGIMBGIcCGLEDGIAEMg0IAhAAGIMBGLEDGIAEMgoIAxAAGLEDGIAEMhMIBBAuGIMBGK8BGMcBGLEDGIoFMgcIBRAAGIAEMg0IBhAAGIMBGLEDGIoFMgcIBxAAGIAEMgoICBAuGLEDGIAEMgcICRAAGI8C0gEIMzc5OWowajmoAgCwAgA&sourceid=chrome&ie=UTF-8"


import qrcode
import random
import sqlite3

var = ""
linkBank = [link1,link2]

var = linkBank[0 + random.randint(0,1)] 
# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
data = var
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a specific folder
folder_path = "C:\\Users\\micha\\OneDrive\\Documents\\Desktop\\scanNlearn\\img_holder"
file_name = "qrcode.png"
img_path = f"{folder_path}/{file_name}"

img.save(img_path)
print(f"QR code saved to: {img_path}")

