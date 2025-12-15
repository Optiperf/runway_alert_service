import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('vishal48@gmail.com', 'xjyp ztpy zoqz hmvf')
server.sendmail('vishal48@gmail.com', 'optiperf@yahoo.com', 'Subject: Test Email\n\nThis is a test email sent from a Python script.')
server.quit()