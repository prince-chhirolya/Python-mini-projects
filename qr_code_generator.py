# import qrcode as qr

# img = qr.make("https://www.linkedin.com/in/prince-chhirolya/")
# img.save("LinkedIn.png")

import qrcode as qr
from PIL import Image

qr = qr.QRCode(version=1, error_correction=qr.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data("https://www.linkedin.com/in/prince-chhirolya/")
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="yellow")
img.save("LinkedIn.png")
