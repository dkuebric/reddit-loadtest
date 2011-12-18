#!/usr/bin/env python

import mechanize
import urllib
import random
from reddit_settings import get_user, put_user, BASE_URL, FORM_DBG

POOL = 'vote_comment'
user = get_user(POOL)
put_user(POOL, user)

class Transaction(object):
    def __init__(self):
        self.custom_timers = {}

    def run(self):
        user = get_user(POOL)
        user.ensure_logged_in()
        br = user.br
        cj = user.cj

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

        # pick a random comment by finding its form -- XXX thread must have ~ 100 comments
        thing_id = None
        tries = 0
        while not thing_id:
            c_num = random.randint(10,90)
            try:
                br.select_form(nr=c_num)
                thing_id = br.form['thing_id']
            except Exception, e:
                # didn't actually find a comment; try again
                if tries > 5:
                    put_user(POOL, user)
                    return
                else:
                    tries += 1
                continue

        # upvote or downvote?
        vote_dir = '1' if random.randint(1,10) < 8 else '-1'

        data = {'uh':uh, 'id':thing_id, 'renderstyle':'html', 'r':rval, 'dir': vote_dir, 'vh': '<$>votehash</$>', }
        new_data_dict = dict((k, urllib.quote(v).replace('%20', '+')) for k, v in data.iteritems())

        new_data = 'id=%(id)s&vh=%(vh)s&dir=%(dir)s&r=%(r)s&uh=%(uh)s&renderstyle=%(renderstyle)s' % (new_data_dict)

        req = mechanize.Request(BASE_URL + '/api/vote', new_data)
        req.add_header('Referer', posting)
        req.add_header('Accept', ' application/json, text/javascript, */*')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
        req.add_header('X-Requested-With', 'XMLHttpRequest')
        cj.add_cookie_header(req)
        res = mechanize.urlopen(req)

        put_user(POOL, user)

if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
