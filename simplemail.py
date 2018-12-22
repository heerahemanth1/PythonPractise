#!/usr/bin/python
# -*- Coding: utf8 -*-

import smtplib, ssl

smtp_server = "localhost"
port = 1025

sender_email = "hh@heerahemanth1.tech"
receiver_email = "shruthichandrasena@gmail.com"
password = input("Email Password: ")
message = '''
Subject: Hey!

How are you, kid?
'''

# Secure SSL context
context = ssl.create_default_context()

# Try logging in and send email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context) # Securing the connection
    server.ehlo()
    server.login(sender_email, password)
    # TODO: Send email here
    server.sendmail(sender_email, receiver_email, message)
except SMTPException as e:
    # Print error messages if any
    print(str(e))
finally:
    server.quit()
