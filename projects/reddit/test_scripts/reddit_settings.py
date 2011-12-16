import mechanize
import cookielib

BASE_URL = 'http://reddit.tracelytics.com'
USER = 'mech1'
PASS = 'asdfjk'

FORM_DBG = 1

def init_browser():
    """Returns an initialized browser and associated cookie jar."""
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    return cj,br

def login(br, u, p):
    r = br.open(BASE_URL)

    # Select the second (index one) form
    br.select_form(nr=1)

    # User credentials
    br.form['user'] = USER
    br.form['passwd'] = PASS

    # Login
    br.submit()
