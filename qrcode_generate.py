#QR code generate
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqr = qrcode.make("https://www.instagram.com/chandra_._shekhar/")
myqr1=qrcode.make("https://www.linkedin.com/in/chandra-shekhar-k/")

myqr.save("myqr.png", scale=8)
myqr1.save("myqr1.png", scale=8)

#decode QR Code
b=decode(Image.open("myqr.png"))
print(b[0].data.decode("ascii"))