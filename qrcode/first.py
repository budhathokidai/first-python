import qrcode

# Data to be encoded
data = "QR Code using make() function"

# Encoding data using make() function
img = qrcode.make("Hello my name is rabi budhathoki <br> well, you know all about me ,yes or know??")

# Saving as an image file
img.save('MyQRCode1.png')