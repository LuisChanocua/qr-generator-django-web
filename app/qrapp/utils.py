import qrcode
from io import BytesIO

def generate_qr_png(content: str, box_size=10, border=2) -> bytes:
    qr = qrcode.QRCode(version=None, box_size=box_size, border=border)
    qr.add_data(content)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()
