import gen_qr 
'''
img = pyqrcode.create('www.facebook.com')
img.svg('abc.svg', scale=10)

'''

qr = gen_qr.QRCode(
    version=1,
    error_correction=gen_qr.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")