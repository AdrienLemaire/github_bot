'''
File: test_bot.py
Author: Adrien Lemaire
Description: Tests for the github bot
'''

from minimock import Mock
import smtplib
from unittest2 import TestCase

from sendMail import sendMail

try:
    from local_settings import SENDER
except:
    import warnings
    warnings.warn("Please create a local_settings.py file")


class TestSendMail(TestCase):

    def setUp(self):
        smtplib.SMTP = Mock('smtplib.SMTP')
        smtplib.SMTP.mock_returns = Mock('smtp_connection')

    def test_sendmail(self):

        result = sendMail(u'Test', SENDER)
