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
        br = init_browser()

        login(br, USER, PASS)
        # TODO

if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
