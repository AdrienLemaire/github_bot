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
from termcolor import colored

# from project
try:
    from local_settings import *  # NOQA
except:
    import warnings
    warnings.warn("Please create a local_settings.py file")


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
        part.add_header('Content-Disposition', 'attachment; filename="%s"' %
            FILE_JOINED)
        msg.attach(part)
    s = smtplib.SMTP(HOST, PORT)
    s.starttls()
    s.login(SENDER, SENDER_PASSWORD)
    s.sendmail(SENDER, recipient, msg.as_string())
    s.quit()
    return "%s %s" % (recipient, colored(" / mail sent !", "green"))
