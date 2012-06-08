#!/usr/bin/env python

import mechanize
import urllib
import random
from util import UserPool, BASE_URL, THREAD

POOL = UserPool()

class Transaction(object):
    def run(self):
        user = POOL.checkout()
        user.ensure_logged_in()
        br = user.br

        # Open up comment page
        posting = THREAD
        rval = THREAD.split('/')[4]
        r = br.open(posting)
        r.read()
        assert (r.code == 200), 'Bad HTTP Response'

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
                    user.checkin()
                    return
                else:
                    tries += 1
                continue

        # upvote or downvote?
        vote_dir = '1' if random.randint(1,10) < 8 else '-1'

        data = {'uh':uh, 'id':thing_id, 'renderstyle':'html', 'r':rval, 'dir': vote_dir, 'vh': '<$>votehash</$>', }
        new_data_dict = dict((k, urllib.quote(v).replace('%20', '+')) for k, v in data.iteritems())

        new_data = 'id=%(id)s&vh=%(vh)s&dir=%(dir)s&r=%(r)s&uh=%(uh)s&renderstyle=%(renderstyle)s' % (new_data_dict)

        r = br.open(BASE_URL + '/api/vote', new_data)
        r.read()
        assert (r.code == 200), 'Bad HTTP Response'

        user.checkin()

if __name__ == '__main__':
    trans = Transaction()
    trans.run()
