from email.mime.image import MIMEImage
from PIL import Image
import io

def attach_company_logo(email):
# Compress and resize the image using Pillow
        logo_path = 'c:/Users/vishu/PycharmProjects/django_hello/runway_alert_service/runways/static/Optiperf-logo-v0.1.png'
        with Image.open(logo_path) as img:
            img = img.convert("RGB")
            img = img.resize((128, 128))
            buffer = io.BytesIO()
            img.save(buffer, format="PNG", optimize=True)
            buffer.seek(0)
            mime_img = MIMEImage(buffer.read())
            mime_img.add_header('Content-ID', '<companylogo>')
            email.attach(mime_img)