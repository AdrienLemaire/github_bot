#!/usr/bin/env python
# -*- coding:Utf-8 -*-
'''
File: github_bot.py
Author: Adrien Lemaire
Description: A small webscraper bot to get an emails' list
'''

from mechanize import Browser
from pyquery import PyQuery as pq
from termcolor import colored
from urllib import unquote
from sendMail import sendMail

try:
    from local_settings import *  # NOQA
except:
    import warnings
    warnings.warn("Please create a local_settings.py file")


def get_email(content):
    email = content(".email").attr("data-email")
    return email and unquote(email) or colored("no email", "red")


def get_fullname(content):
    """scrape fullname from user page and return it"""
    return content('span[itemprop="name"]').html() or ""


def get_pages_count(content):
    """scrape pagination from search results page and return it"""
    pagination = content('.pagination').text()
    return pagination and int(pagination.split()[-1]) or 1

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


def search(br, type_search, language, location):
    """Search the contacts according to your criteria"""

    global PAGE_START, USER_START
    user_nb = 0  # counter
    pages_count = 0

    while True:
        br.select_form(nr=0)
        br.set_all_readonly(False)
        br.form.new_control('text', 'language', {'value': language})
        try:
            """The search from the home page requires a string"""
            br['type'] = type_search
        except:
            """After, when we are in the search page, it requires a sequence"""
            br['type'] = [type_search]
        br['start_value'] = str(PAGE_START)
        br['q'] = 'location:%s' % location
        try:
            request = br.submit()
        except:
            print colored('Page not found', 'red')
            print br.title()
            br.back()
            continue

        page = pq(request.read())
        if not pages_count:
            pages_count = get_pages_count(page)
            print colored('Search has %s pages of results' % pages_count,
                'blue')
        for nickname in page('.result a').map(lambda i, a: pq(a).text()):
            message = '%s => ' % colored(nickname, 'blue')
            user_nb += 1
            for link in br.links():
                if nickname in link.text:
                    request = br.follow_link(link)
                    content = pq(request.read())
                    fullname = get_fullname(content)

                    if user_nb < USER_START:
                        message += colored('not authorized ...', 'blue')
                        continue

                    email = get_email(content)
                    if email:
                        #message += 'fake email sent'
                        message += sendMail(fullname, email)
            print message
            br.back()

        if PAGE_START == pages_count:
            # End of search
            break
        PAGE_START += 1
        print colored('Go to page %d' % PAGE_START, 'blue')


if __name__ == '__main__':
    #br = github_login(username, password)
    br = github_connect()
    search(br, TYPE_SEARCH, TYPE_LANGUAGE, LOCATION)
