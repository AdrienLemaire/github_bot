#!/usr/bin/env python
# -*- coding:Utf-8 -*-
'''
File: github_bot.py
Author: Adrien Lemaire
Description: A small webscraper bot to get an emails' list
'''

# from python
import logging
from mechanize import Browser
from pyquery import PyQuery as pq
from termcolor import colored
from urllib import unquote
from sendMail import sendMail
from sys import stdout

# from project
try:
   from local_settings import *
except:
   import warnings
   warnings.warn("Please change you local settings file to be called "\
                 "local_settings.py")


def github_connect(path=""):
    """Connect to the website"""
    br = Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Firefox')]
    br.open('https://github.com/%s' % path)
    return br


def github_login(login, password):
    """login, you don't need it to perform a research"""
    br = github_connect("login")
    br.select_form(nr=1)
    br['login'] = login
    br['password'] = password
    br.submit()
    return br


def search(type, language, location):
    """Search the contacts according to your criteria"""

    global PAGE_START, USER_START
    user_nb = 0 # counter

    while True:
        br.select_form(nr=0)
        br.set_all_readonly(False)
        br.form.new_control('text', 'language', {'value': language})
        try:
            """The search from the home page requires a string"""
            br['type'] = type
        except:
            """After, when we are in the search page, it requires a sequence"""
            br['type'] = [type]
        br['start_value'] = str(PAGE_START)
        br['q'] = 'location:%s' % location
        request = br.submit()
        page = pq(request.read())
        pagination = page('.pagination').text()
        pages_count = int(pagination[-1]) if pagination else 1
        for nickname in page('.result a').map(lambda i, a: pq(a).text()):
            message = colored(nickname, "blue") + " => "
            user_nb += 1
            for link in br.links():
                if nickname in link.text:
                    try:
                        request = br.follow_link(link)
                        content = pq(request.read())
                        fullname = content('span[itemprop="name"]').html() or ""
                        if user_nb >= USER_START:
                            try:
                                email = unquote(content(".email").attr("data-email"))
                                #sendMail(fullname, email)
                                message += email + \
                                        colored(" / mail sent !", "green")
                            except:
                                message += colored("no email", "red")
                        else:
                            message += colored("not authorized ...", "blue")
                    except:
                        message += colored("no page", "red")
                    break
            print message
            br.back()

        if PAGE_START == pages_count:
            break
        PAGE_START += 1


#br = github_login(username, password)
br = github_connect()
search(TYPE_SEARCH, TYPE_LANGUAGE, LOCATION)
