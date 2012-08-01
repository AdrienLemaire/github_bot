#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
File: sendMail.py
Author: Adrien Lemaire
Description: Send an email to seek after a job from my gmail account
'''

# from python
from email import Encoders
from email.Header import Header
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# from project
try:
   from local_settings import *
except:
   import warnings
   warnings.warn("Please change you local settings file to be called "\
                 "local_settings.py")



def sendMail(fullname, recipient, encoding="utf-8"):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = Header(MAIL_TITLE.encode(encoding), encoding)
    msg['From'] = SENDER
    msg['To'] = recipient
    text = u"%s %s,\n%s" % (
        MAIL_HELLO,
        fullname or "",
        MAIL_MESSAGE,
    )
    msg.attach(MIMEText(text.encode(encoding), 'plain', encoding))
    # Attach file if specified
    if FILE_JOINED:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(FILE_JOINED, "rb").read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; ' +\
            'filename="' + FILE_JOINED + '"')
        msg.attach(part)
    s = smtplib.SMTP(HOST, PORT)
    s.starttls()
    s.login(SENDER, SENDER_PASSWORD)
    s.sendmail(SENDER, recipient, msg.as_string())
    s.quit()

sendMail(u'Test', SENDER)  # test
