import mechanize
import time


class Transaction(object):
    def __init__(self):
        self.custom_timers = {}
        self.base_url = 'http://reddit.tracelytics.com'
    
    def run(self):
        br = mechanize.Browser()
        br.set_handle_robots(False)
        
        start_timer = time.time()
        resp = br.open(self.base_url + '/r/all/')
        resp.read()
        latency = time.time() - start_timer
        self.custom_timers['All_Items'] = latency  
        assert (resp.code == 200), 'Bad HTTP Response'
        

if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
