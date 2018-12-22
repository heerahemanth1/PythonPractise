#!/usr/bin/python
# -*- Coding: utf8 -*-

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "hh@heerahemanth1.tech"
receiver_email = "shruthichandrasena@gmail.com"
password = input("Password: ")

message = MIMEMultipart("alternative")
message["Subject"] = "Thinking about you."
message["From"] = sender_email
message["To"] = receiver_email

# Plain text and HTML version of the message
text = """\
        Hi,
        How are you?"""
html = """\
        <html>
        <body>
        <p>Hi,<br>
        How are you?<br>
        <a href="http://www.realpython.com">Real Python</a>
        has many great tutorials.
        </p>
        </body>
        </html>
        """

# Generate text/mime objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Append email content to multipart message object
message.attach(part1)
message.attach(part2)

# Create a secure connection with the server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("localhost", 1025, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

