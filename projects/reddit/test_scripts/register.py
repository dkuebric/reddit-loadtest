#!/usr/bin/env python

import mechanize
import cookielib
import urllib
import logging
import sys
import time
from reddit_settings import *

class Transaction(object):
    def __init__(self):
        self.custom_timers = {}

    def run(self):
        (cj, br) = init_browser()

        br.open(BASE_URL)

        br.select_form(predicate=lambda f: 'id' in f.attrs and f.attrs['id'] == 'login_reg')
        br.form['user'] = 'mech2'
        br.form['passwd'] = 'reddit'
        br.form['passwd2'] = 'reddit'
        br.submit()

if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
