# Generate QR Code for website
# Also possible from the command line directly: qr "firewise.mtbacheloma.org" > qr.png

from PIL import Image
import qrcode

qr = qrcode.make('firewise.mtbacheloma.org')
type(qr)  # qrcode.image.pil.PilImage
qr.save("zCode/qr.png")

qr = qr.resize((1500,1500))
qr.save("zCode/qr_resize.pdf")
qr.save("zCode/qr_resize.png")