import argparse
import requests
import pycurl
from time import sleep
 
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--foreground",  action="store_true")
args = parser.parse_args()

def do_job():
    info = requests.get('http://ukr.net/')
    print info
def getUserData():
	c = pycurl.Curl()
	c.setopt(pycurl.URL, 'https://ukr.net')
	c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
	c.setopt(pycurl.USERPWD, 'username:userpass')
	c.perform()
if args.foreground:
    print "Foreground option"
    while 1:
    	do_job()
    	getUserData()
    	sleep(5)
else:
    print "Foreground option was not passed, going to be a daemon"
    do_job()
