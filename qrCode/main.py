import qrcode
import PIL

img = qrcode.make("https://ramandeepsingh2402.github.io/portfolio/")

img.save("qrcode.jpg")
