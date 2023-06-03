import qrcode

from consts import *

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=1,
    border=0,
)
qr.add_data(FLAG_TEXT)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

type(img)  # qrcode.image.pil.PilImage

img.save(RESULT_FILE_NAME)
