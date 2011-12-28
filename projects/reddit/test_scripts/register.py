#!/usr/bin/env python

import mechanize
import cookielib
import urllib
import logging
import sys
import time
import random
from util import _init_browser, BASE_URL

class Transaction(object):
    def __init__(self):
        self.custom_timers = {}

    def run(self, basename='onetime_', num=1, predictable=False):
        for i in xrange(num):
            uname = basename + str(i+1)
            if not predictable:
                uname += random.randint(1, 10000)

            (cj, br) = _init_browser()

            br.open(BASE_URL)
            br.select_form(predicate=lambda f: 'id' in f.attrs and f.attrs['id'] == 'login_reg')
            br.form['user'] = uname
            br.form['passwd'] = 'reddit'
            br.form['passwd2'] = 'reddit'
            r = br.submit()
            r.read()
            assert (r.code == 200), 'Bad HTTP Response'
            print "Created user " + uname

if __name__ == '__main__':
    trans = Transaction()
    if len(sys.argv) == 3:
        # generate predictably-named users for use in tests
        basename = sys.argv[1]
        num = int(sys.argv[2])
        trans.run(basename, num, True)
    else:
        trans.run()
    print trans.custom_timers
