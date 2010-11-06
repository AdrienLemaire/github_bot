#!/usr/bin/python
# -*- coding:Utf-8 -*-
'''
File: sendMail.py
Author: Adrien Lemaire
Description: Send an email to seek after a job from my gmail account
'''

# from python
from email import Encoders
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



def sendMail(fullname, recipient):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = MAIL_TITLE
    msg['From'] = SENDER
    msg['To'] = recipient
    try:
        """If there are not-utf8 characters, we exclude the name"""
        MIMEText(fullname, 'plain')
    except:
        fullname = ""
    text = "Hi %s,\n%s" % (fullname or "", MAIL_MESSAGE)
    msg.attach(MIMEText(text, 'plain'))
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

#sendMail(u'Adrien', SENDER)  # test
