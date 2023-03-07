import qrcode
import base64
import io


def new_qr_code(totp_uri: str) -> str:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2
    )
    qr.add_data(totp_uri)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = io.BytesIO()
    img.save(buffer, "PNG")
    imageB64 = base64.b64encode(buffer.getvalue()).decode("ascii")

    return imageB64
