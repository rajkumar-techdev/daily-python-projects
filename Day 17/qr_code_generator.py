import qrcode

def generate_qr():

    data=input("Enter the Text or URl to generate QR Code: ").strip()
    filename=input("Enter file name to save:  ").strip()

    qr=qrcode.make(data)
    qr.save(f"{filename}.png")

    print(f"QR code Saved as {filename}.png")

generate_qr()

