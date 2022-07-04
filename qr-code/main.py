import qrcode

data = 'https://github.com/dcartwright07'

qr = qrcode.QRCode(
    version = 1,
    box_size = 10,
    border = 5
)
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color = (145, 15, 35), back_color = 'white')
image.save('myqrcode.png')
