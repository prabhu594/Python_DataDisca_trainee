import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

email_user = 'spm2640@gmail.com'
email_send = 'spm2640@gmail.com'
subject = 'Server Performance'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Processor and Memmory Usage'
msg.attach(MIMEText(body,'plain'))

filename = 'document.txt'
attachment = open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,'your_password')


server.sendmail(email_user,email_send,text)
server.quit()
