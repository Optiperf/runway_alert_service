from django.core.mail import send_mail
from django.core.mail import EmailMessage

from .image_service import attach_company_logo

def send_email(runways, request):
# Send email if POST request
    if request.method == 'POST':
        email_body = """
        <div style="text-align:center;">
        <h2>Runway Status</h2>
        <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; margin: 0 auto;" align="center">
            <tr>
                <th>Runway Name</th>
                <th>Activity</th>
            </tr>
        """
        for runway in runways:
            if runway['activity'] == 'Silent':
                color = 'gray'
            elif runway['activity'] == 'Take-off':
                color = 'blue'
            elif runway['activity'] == 'Landing':
                color = 'green'
            else:
                color = 'black'
            email_body += f"""
            <tr>
                <td>{runway['name']}</td>
                <td style="color:{color};">{runway['activity']}</td>
            </tr>
            """
        email_body += """
        </table>
        <br><br>
        <p>Powered by:</p>
        <img src="cid:companylogo" width="128" height="128" style="border-radius:8px; display:block; margin:0 auto;" alt="Company Logo"/>
        </div>
        """

        email = EmailMessage(
            subject='Runway Status Report',
            body=email_body,
            from_email=None,
            to=['optiperf@yahoo.com'],
        )
        email.content_subtype = "html"

        attach_company_logo(email)

        email.send(fail_silently=False)