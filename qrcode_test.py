import qrcode
import sys
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(sys.argv[1])
qr.make(fit=True)
img = qr.make_image()
img.save('test.png')