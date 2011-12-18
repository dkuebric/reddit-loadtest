#!/usr/bin/env python
# some parts from http://stackoverflow.com/questions/4720470/using-python-and-mechanize-to-submit-form-data-and-authenticate

import mechanize
import urllib
from reddit_settings import *

class Transaction(object):
    def __init__(self):
        self.custom_timers = {}

    def run(self):
        cj,br = init_browser()

        user = get_user('submit_comment')

        login(br, user, PASS)

        # Open up comment page
        posting = BASE_URL + '/r/reddit_test6/comments/2d/httpgooglecomq376080238706/?'
        rval = 'reddit_test6'
        # you can get the rval in other ways, but this will work for testing

        r = br.open(posting)

        if FORM_DBG:
            i = 0
            for e in br.forms():
                print i, e
                i += 1

        # You need the 'uh' value from the first form
        br.select_form(nr=0)
        uh = br.form['uh']

        br.select_form(nr=12)
        thing_id = br.form['thing_id']
        id = '#' + br.form.attrs['id']
        # The id that gets posted is the form id with a '#' prepended.

        data = {'uh':uh, 'thing_id':thing_id, 'id':id, 'renderstyle':'html', 'r':rval, 'text':"This is such an interesting comment!  Upboat me!"}
        new_data_dict = dict((k, urllib.quote(v).replace('%20', '+')) for k, v in data.iteritems())

        # not sure if the replace needs to happen, I did it anyway
        new_data = 'thing_id=%(thing_id)s&text=%(text)s&id=%(id)s&r=%(r)s&uh=%(uh)s&renderstyle=%(renderstyle)s' %(new_data_dict)

        # not sure which of these headers are really needed, but it works with all
        # of them, so why not just include them.
        req = mechanize.Request(BASE_URL + '/api/comment', new_data)
        req.add_header('Referer', posting)
        req.add_header('Accept', ' application/json, text/javascript, */*')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
        req.add_header('X-Requested-With', 'XMLHttpRequest')
        cj.add_cookie_header(req)
        res = mechanize.urlopen(req)

        put_user('submit_comment', user)

if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
