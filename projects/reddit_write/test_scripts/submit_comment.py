#!/usr/bin/env python
# some parts from http://stackoverflow.com/questions/4720470/using-python-and-mechanize-to-submit-form-data-and-authenticate

import mechanize
import urllib
from util import UserPool, BASE_URL, THREAD

POOL = UserPool()

class Transaction(object):
    def run(self):
        user = POOL.checkout()
        user.ensure_logged_in()
        br = user.br
        cj = user.cj

        # Open up comment page
        posting = THREAD
        rval = THREAD.split('/')[4]
        r = br.open(posting)
        r.read()
        assert (r.code == 200), 'Bad HTTP Response'

        br.select_form(nr=0)
        uh = br.form['uh']

        br.select_form(nr=12)
        thing_id = br.form['thing_id']
        id = '#' + br.form.attrs['id']

        data = {'uh':uh, 'thing_id':thing_id, 'id':id, 'renderstyle':'html', 'r':rval, 'text':"This is such an interesting comment!  Upboat me! x"}
        new_data_dict = dict((k, urllib.quote(v).replace('%20', '+')) for k, v in data.iteritems())
        new_data = 'thing_id=%(thing_id)s&text=%(text)s&id=%(id)s&r=%(r)s&uh=%(uh)s&renderstyle=%(renderstyle)s' %(new_data_dict)

        r = br.open(BASE_URL + '/api/comment', new_data)
        r.read()
        assert (r.code == 200), 'Bad HTTP Response'

        user.checkin()

if __name__ == '__main__':
    trans = Transaction()
    trans.run()
