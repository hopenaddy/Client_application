import argparse
import requests
from daemonize import Daemonize
import json
from time import sleep
import getpass
import pycurl

URL_ADDRESS = 'http://lv128.tk:8813/'
URL_Listener = 'http://lv128.tk:8813/'
URL_ADDRESS = "http://client.lv128.tk/login"
URL_Listener = 'http://hl.lv128.tk/'
>>>>>>> 0626a3696b56e6549524bb77e16538e2bf0aad0d
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
    """
    Auth on nd with login, pass, token:

    c = pycurl.Curl()
    params = {  "login":"root",
                "pass":"1",
                "token":"06df9d21-f727-44df-b6c4-5bbd127479e5",
                "n":"3"
        }
    para = "&".join(["%s=%s" % (k, v) for k, v in params.items()])  
    c.setopt(pycurl.URL, 'lv128.tk:8813')
    c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
    c.setopt(pycurl.POSTFIELDS, para)
    c.setopt(pycurl.POST, 1)
    c.perform()
"""
def send_message():
    msg = raw_input('Input your message:')
    token = 'DevToken'
    url = 'http://hl.lv128.tk/'
    sender.setopt(sender.URL, str(url))
    token = 'some_token'
    sender.setopt(sender.URL, str(URL_Listener))
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
        auth()
        send_message()
