Github Bot
----------

Useful bot to exploit the github search box in a large scale and send email to
the users.


.. warning:: *Ethical Concerns*

    Please do not use that bot for spam, or you might get your account suspended
    by Github, cf the ToS.

    I personally only use it to ask some developers if they know of
    job opportunities for me. I could mail each of them manually, but I value my
    time, and this application is an excellent case to show my skills.
    Also note that the Github API allows to get the name / email of a github
    user (I just wrote that bot before the Github API got release)


Dependencies
+++++++++++++

Make sure that you have a working Python_ 2.x >= 2.6::

    $ mkvirtualenv -p python2 github_bot
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
    * **SENDER_PASSWORD**
    * **HOST** (e.g. smtp.gmail.com)
    * **PORT** (e.g 587 for google)
 - your message
    * **FILE_JOINED** (path to the file)
    * **MAIL_TITLE**
    * **MAIL_MESSAGE**

A local_settings.py.sample file is available for commodity, so you can::

    $ cp local_settings.py.sample local_settings.py


Then you can run the project::

    $ python github_bot.py


.. _Python: http://python.org
