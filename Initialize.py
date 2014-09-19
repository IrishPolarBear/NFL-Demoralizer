#from urllib2 import urlopen, URLError, HTTPError
import urllib.request
import urllib.error
class Initialize:

    def __init__(self):
        url = 'http://www.nfl.com/'
        try:
            response = urllib.request.urlopen(url)
        except urllib.error.HTTPError as e:
            self.server = "Unable to Connect with Server"
        except urllib.error.HTTPError as e:
            self.server = "Unable to Reach Server"
        else:
            self.server = "Success"
    
