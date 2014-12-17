import argparse
import requests
from daemonize import Daemonize
import json
from time import sleep
import getpass
import pycurl

URL_ADDRESS = "http://client.lv128.tk/login"
URL_Listener = 'http://hl.lv128.tk/'
PID_FILE = "/tmp/test.pid"
sender = pycurl.Curl()

new_status = requests.get(URL_ADDRESS) 
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--foreground",  action="store_true")
args = parser.parse_args()

def getStatus():
    return new_status.status_code
    
def auth():
    login = raw_input('Login:')
    password = getpass.getpass()
    payload = {'Username:': login,'Password:':password}
    headers = {'content-type': 'application/json'}
    r = requests.post(URL_ADDRESS, data=json.dumps(payload), headers=headers)
    print r.content

def send_message():
    msg = raw_input('Input your message:')
    token = 'some_token'
    sender.setopt(sender.URL, str(URL_Listener))
    sender.setopt(sender.POSTFIELDS, 'msg=' + msg + '&token=' + token)
    #sender.perform()
    print "OK! You sended your message"
    
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
        auth()
        send_message()
