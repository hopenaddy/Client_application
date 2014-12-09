import argparse
import os
import requests
import pycurl
from daemonize import Daemonize
from time import sleep

URL_ADDRESS = "http://lv128.tk:15672"
PID_FILE = "/tmp/test.pid"

new_status = requests.get(URL_ADDRESS) 
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--foreground",  action="store_true")
args = parser.parse_args()

def getStatus():
    return new_status.status_code
    
def getUserData():
    r = requests.get(URL_ADDRESS)
    head = r.headers
    for key, value in head.iteritems() :
        print key, value
    
def mytest():
    while 1:
        print getStatus()
        getUserData()
        sleep(5)

if __name__ == "__main__":
    if args.foreground:
        daemon = Daemonize(app="test_app", pid=PID_FILE, action=mytest)
        daemon.start()
    else:
        print getStatus()
        getUserData()
