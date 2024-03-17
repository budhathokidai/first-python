import qrcode

# Data to be encoded
data = "QR Code using make() function"

# Encoding data using make() function
img = qrcode.make("Hello my name is rabi budhathoki.\
                   i am 19 years old and am  from ramechhape district.\
                  i completed my school level from 'Emmanuel english boarding school', my intermediate level from 'Khwopa secondary school' and currently studying my bachlor level in 'Sanothimi campus'.\
                  if u want to contact me... \
                  phone no:'9849737558' and Email : rabibudhathoki83@gmail.com")

# Saving as an image file
img.save('MyQRCode1.png')