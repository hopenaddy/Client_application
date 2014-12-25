import argparse
import requests
from daemonize import Daemonize
import json
from time import sleep
import getpass
import pycurl

URL_ND = 'http://lv128.tk:8813/'
URL_ADDRESS = "http://client.lv128.tk/login"
URL_LiSTENER = 'http://hl.lv128.tk/'
PID_FILE = "/tmp/test.pid"
sender = pycurl.Curl()

new_status = requests.get(URL_ND) 
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--foreground",  action="store_true")
args = parser.parse_args()

def getStatus():
    return new_status.status_code
    
def get_user_msgs():
    login = raw_input('Login:')
    password = getpass.getpass()
    c = pycurl.Curl()
    params = {  "login":login,
                "pass":password,
                #"token":"06df9d21-f727-44df-b6c4-5bbd127479e5",
                #"n":"3"
        }
    para = "&".join(["%s=%s" % (k, v) for k, v in params.items()])  
    c.setopt(pycurl.URL, URL_ND)
    c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
    c.setopt(pycurl.POSTFIELDS, para)
    c.perform()
def auth():
    login = raw_input('Login:')
    password = getpass.getpass()
    payload = {'Username:': login,'Password:':password}
    headers = {'content-type': 'application/json'}
    r = requests.post(URL_ADDRESS, data=json.dumps(payload), headers=headers)
    print r.content

def send_message():
    msg = raw_input('Input your message:')
    token = raw_input('Input your token:')
    if (token == ''):
        token = 'DevToken'
    sender.setopt(sender.URL, str(URL_LiSTENER))
    sender.setopt(sender.POSTFIELDS, 'msg=' + msg + '&token=' + token)
    sender.perform()
    print "OK! You sended your message"
    
def func_for_daemon():
    while 1:
        print getStatus()
        sleep(5)

if __name__ == "__main__":
    if args.foreground:
         daemon = Daemonize(app="test_app", pid=PID_FILE, action=mytest)
         daemon.start()
    else:
        print getStatus()
        get_user_msgs()
        print '\n'
        send_message()
