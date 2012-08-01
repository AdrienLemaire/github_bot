'''
File: test_bot.py
Author: Adrien Lemaire
Description: Tests for the github bot
'''

# from project
try:
    from local_settings import SENDER
except:
   import warnings
   warnings.warn("Please create a local_settings.py file")


class TestSendMail:

    def test_sendmail(self):
        sendMail(u'Test', SENDER)
