#!/usr/bin/python
# -*- Coding: utf8 -*-
Sat Dec 22 19:54:10 IST 2018

import smtplib, ssl, os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "hh@heerahemanth1.tech"
receiver_email = "shruthichandrasena@gmail.com"
password = input("Password: ")

message = MIMEMultipart()
message["Subject"] = "Thinking about you."
message["From"] = sender_email
message["To"] = receiver_email

# Plain text and HTML version of the message
text = """\
        Hi,
        How are you?"""

# Generate text/mime objects
part1 = MIMEText(text, "plain")

# Append email content to multipart message object
message.attach(part1)

# Append attachment file
filename = os.path.join(os.path.expanduser("~"),"/Documents/infatuation.doc")
with open(filename, 'rb') as attachment:
    # add file as application/octet-stream
    # email client can download it automatically
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode attachment in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key-value pair to attachment part
part.add_header(
        "Content-Disposition",
        f"attachment; filename={filename}",
)

# Add attachment to the message
message.attach(part)
text = message.as_string()

# Create a secure connection with the server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("localhost", 1025, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

