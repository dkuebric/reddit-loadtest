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

    def run(self, basename='user_', num=1):
        for i in xrange(num):
            uname = basename + str(i+1)

            (cj, br) = init_browser()

            br.open(BASE_URL)
            br.select_form(predicate=lambda f: 'id' in f.attrs and f.attrs['id'] == 'login_reg')
            br.form['user'] = uname
            br.form['passwd'] = 'reddit'
            br.form['passwd2'] = 'reddit'
            br.submit()
            print "Created user " + uname

if __name__ == '__main__':
    trans = Transaction()
    if len(sys.argv) == 3:
        basename = sys.argv[1]
        num = int(sys.argv[2])
        trans.run(basename, num)
    else:
        trans.run()
    print trans.custom_timers
