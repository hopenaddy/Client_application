import argparse
import requests
import pycurl
from time import sleep

status = requests.get('http://ukr.net/') 
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--foreground",  action="store_true")
args = parser.parse_args()

def getstatus(status):
    return status
def getUserData():
	c = pycurl.Curl()
	c.setopt(pycurl.URL, 'https://ukr.net')
	c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
	c.setopt(pycurl.USERPWD, 'username:userpass')
	c.perform()
	    
if __name__ == "__main__":
	if args.foreground:
    		print "Foreground option"
    		while 1:
    		getstatus()
    		getUserData()
    		sleep(5)
	else:
    	print "Foreground option was not passed, going to be a daemon"
    	getstatus()

	
