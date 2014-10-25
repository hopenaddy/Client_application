import argparse
import requests
import pycurl
 
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
    do_job()
    getUserData()
else:
    print "Choose argument"
    do_job()
