'''
File: test_bot.py
Author: Adrien Lemaire
Description: Tests for the github bot
'''

from minimock import Mock
from pyquery import PyQuery as pq
import smtplib
from unittest2 import TestCase

from github_bot import get_fullname, get_email, github_connect
from sendMail import sendMail

try:
    from local_settings import SENDER
except:
    import warnings
    warnings.warn('Please create a local_settings.py file')


class TestSendMail(TestCase):

    def setUp(self):
        smtplib.SMTP = Mock('smtplib.SMTP')
        smtplib.SMTP.mock_returns = Mock('smtp_connection')

    def test_sendmail_succeeds(self):
        result = sendMail(u'Test', SENDER)
        self.assertEquals(result, '%s \x1b[32m / mail sent !\x1b[0m' % SENDER)


class TestScraper(TestCase):

    def setUp(self):
        self.request = github_connect(path='Fandekasp')

    def test_can_connect(self):
        request = github_connect()
        self.assertEquals(request.title(), 'GitHub \xc2\xb7 Social Coding')

    def test_fullname(self):
        """test that our query selection for full name is still valid"""
        page = pq(self.request.response().read())
        self.assertEquals(get_fullname(page), 'Adrien Lemaire')

    def test_email(self):
        """test that our query selection for email is still valid"""
        page = pq(self.request.response().read())
        self.assertEquals(get_email(page), 'lemaire.adrien@gmail.com')
