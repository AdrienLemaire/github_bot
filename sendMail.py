#!/usr/bin/python
# -*- coding:Utf-8 -*-
'''
File: sendMail.py
Author: Adrien Lemaire
Description: Send an email to seek after a job from my gmail account
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import Encoders


def sendMail(fullname, email):
    file = "CV Adrien Lemaire.06_2010.pdf" # Change by your own file
    sender = "lemaire.adrien@gmail.com" # put your email here
    recipient = email
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Seeking for a job in Python Software Development'
    msg['From'] = sender
    msg['To'] = recipient
    text = "Hi " + fullname + ",\n\n" +\
        "I'm Adrien LEMAIRE, 22 years old, student in the french Computer " +\
        "Science school called SUPINFO. I'm currently finishing my school " +\
        "year in San Francisco, and I'll go in London (campus located on " +\
        "32, Lombard Street) to get my master. I'll probably arrive in " +\
        "London starting in July 10th, so I'm seeking for a job in Python " +\
        "Software Development there.\n\n" +\
        "I found your email searching for Python developer based in London" +\
        " on Github (mine is 'Fandekasp'). If you are aware of " +\
        "opportunities for me, I will be very grateful for your help.\n\n" +\
        "Please find inclosed my CV, and I can give more explanations " +\
        "about my python skills if you want me to.\n\n" +\
        "Thank you very much, and sorry for the disturb in any case,\n" +\
        "Sincerely,\nAdrien LEMAIRE"
    msg.attach(MIMEText(text, 'plain'))
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(file, "rb").read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; ' +\
        'filename="' + file + '"')
    msg.attach(part)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("lemaire.adrien@gmail.com", "password")
    s.sendmail(sender, recipient, msg.as_string())
    s.quit()