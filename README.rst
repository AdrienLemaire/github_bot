Github Bot
----------

Useful bot to exploit the github search box in a large scale and send email to
the users.


Dependencies
+++++++++++++

Make sure that you have a working Python_ 2.x >= 2.6::

    $ pip install -r requirements.txt


How to use
+++++++++++

You have to create a ``local_settings.py`` file and fill the following variables

 - github account
    * **USERNAME**
    * **PASSWORD**
 - search informations
    * **TYPE_SEARCH** (e.g. "Users")
    * **TYPE_LANGUAGE** (e.g. "Python")
    * **LOCATION** (e.g. "London")
    * **PAGE_START** (first page to send mail, usually = 1)
    * **USER_START** (first user of the PAGE_START to send mail, usually = 1)
 - your email
    * **SENDER**
    * **EMAIL_PASSWORD**
    * **HOST** (e.g. smtp.gmail.com)
    * **PORT** (e.g 587 for google)
 - your message
    * **FILE_JOINED** (path to the file)
    * **MAIL_TITLE**
    * **MAIL_MESSAGE**

Then you just have to run the project::

    $ python github_bot.py


.. _Python: http://python.org
