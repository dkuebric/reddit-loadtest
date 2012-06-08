import cookielib
import mechanize
import weakref
from reddit_settings import *

class UserPool(object):
    def __init__(self, size=MAX_THREADS, basename=BASE_USERNAME):
        self.in_users = []
        self.out_users = {}
        for i in xrange(size):
            uname = basename + str(i+1)
            print "Filling pool with", uname
            br = _init_browser()
            u = User(uname, br, self)
            self.in_users.append(u)

    def checkout(self):
        u = self.in_users.pop()
        self.out_users[u] = True
        return u

    def checkin(self, u):
        del self.out_users[u]
        self.in_users.append(u)

class User(object):
    def __init__(self, user, br, pool):
        self.user = user
        self.br = br
        self.logged_in = False
        self.pool = weakref.proxy(pool)

    def ensure_logged_in(self):
        if not self.logged_in:
            _login(self.br, self.user, PASS)
            self.logged_in = True
        return

    def checkin(self):
        self.pool.checkin(self)

    def __str__(self):
        return "User<user=%s,logged_in=%s>" % (self.user, self.logged_in)

# utility functions
def _init_browser():
    """Returns an initialized browser and associated cookie jar."""
    br = mechanize.Browser()

    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    return br

def _login(br, u, p):
    _ = br.open(BASE_URL)

    br.select_form(nr=1)
    br.form['user'] = u
    br.form['passwd'] = p
    r = br.submit()
    r.read()
    assert (r.code == 200), 'Bad HTTP Response'
