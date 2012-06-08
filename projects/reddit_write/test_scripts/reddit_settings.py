###############################################################################
# Settings file for reddit load tests
###############################################################################

# base URL of installation
BASE_URL = 'http://reddit.tlys.us'

# the maximum number of threads you plan to run for each test
# (specifies user pool size for each test script)
MAX_THREADS = 50

# pre-generated users up to 100 -- must be created by running register.py manually
BASE_USERNAME = 'user_'

# password for all generated users
PASS = 'reddit'


# comment for submit_comment and vote_comment tests
THREAD = BASE_URL + '/r/reddit_test7/comments/2q/httpgooglecomq366843696587/'
