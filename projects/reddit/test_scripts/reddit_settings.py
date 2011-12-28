###############################################################################
# Settings file for reddit load tests
###############################################################################

# base URL of installation
BASE_URL = 'http://ec2-50-17-153-135.compute-1.amazonaws.com'

# the maximum number of threads you plan to run for each test
# (specifies user pool size for each test script)
MAX_THREADS = 50

# pre-generated users up to 100 -- must be created by running register.py manually
BASE_USERNAME = 'user_'

# password for all generated users
PASS = 'reddit'


# comment for submit_comment and vote_comment tests
THREAD = BASE_URL + '/r/reddit_test6/comments/22/httpgooglecomq392636488427/'
