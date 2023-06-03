import qrcode
from PIL import Image


class QrCode:
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename

    def generate_qr(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(self.filename)

    def show_qr(self):
        img = Image.open(self.filename)
        img.show()


def main():
    qr = QrCode("https://github.com/YavuzMuratt", "github.png")
    qr.generate_qr()

    qr.show_qr()


if __name__ == "__main__":
    main()
