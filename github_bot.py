#!/usr/bin/python
# -*- coding:Utf-8 -*-
'''
File: github_bot.py
Author: Adrien Lemaire
Description: A small webscraper bot to get an emails' list
'''

from mechanize import Browser
from urllib import unquote
from pyquery import PyQuery as pq
from sys import stdout
import logging
from termcolor import colored
from sendMail import sendMail


def github_connect():
    """Connect to the website"""
    br = Browser()
    br.addheaders = [('User-agent', 'Firefox')]
    requete = br.open('https://github.com/login')
    return br


def github_login(login, password):
    """login, you don't need it to perform a research"""
    br = github_connect()
    d = pq(requete.read())
    br.select_form(nr=1)
    br['login'] = login
    br['password'] = password
    br.submit()
    return br


def search(type, language, location):
    """Search the contacts according to your criteria"""
    page_nb = 1
    while True:
        br.select_form(nr=0)
        br.set_all_readonly(False)
        br.form.new_control('text', 'language', {'value': language})
        br['type'] = type
        br['start_value'] = str(page_nb)
        br['q'] = 'location:' + location
        request = br.submit()
        d = pq(request.read())
        pages_count = int(d('.pagination').text().split()[-1])
        for nickname in d('.result a').map(lambda i, a: pq(a).text()):
            message = colored(nickname, "blue") + " => "
            for link in br.links():
                if nickname in link.text:
                    try:
                        request = br.follow_link(link)
                        d = pq(request.read())
                        try:
                            message += unquote(d('.email').text().split("'")\
                                    [-2]).split(">")[1].split("<")[0]
                        except:
                            message += colored("no email", "red")
                    except:
                        message += colored("no page", "red")
                    break
            print message
            br.back()

        if page_nb == pages_count:
            break
        page_nb += 1


#br = github_login("Fandekasp", "password")
br = github_connect()
search('Users', 'python', 'London')
