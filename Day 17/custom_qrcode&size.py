import qrcode
from PIL import Image
from qrcode.console_scripts import error_correction

def custom_qr():
    qr=qrcode.QRCode(
         version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
         box_size=10,
         border=4,

)

    data=input("Enter a text or URL to generate QR Code")
    qr.add_data(data)
    qr.make(fit=True)

    img=qr.make_image(fill_color="orange",back_color="black")
    img.save("custom_qr.png")


custom_qr()