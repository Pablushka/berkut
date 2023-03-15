import qrcode
import base64
import io


def new_qr_code(totp_uri: str) -> str:

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(totp_uri)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffered = io.BytesIO()
    img.save(buffered, "PNG")

    img_str = base64.b64encode(buffered.getvalue()).decode("ascii")

    return img_str
