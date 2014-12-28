import json
import getpass
import argparse
import requests
from time import sleep
from daemonize import Daemonize

URL_ND = 'http://lv128.tk:8813/'
URL_ADDRESS = "http://client.lv128.tk/login"
URL_LiSTENER = 'http://hl.lv128.tk/'
PID_FILE = "/tmp/test.pid"

new_status = requests.get(URL_ND) 
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--foreground",  action="store_true")
parser.add_argument("-send", "--send_msg", action="store_true")
args = parser.parse_args()

def getStatus():
    return new_status.status_code

login = raw_input('Login:')
password = getpass.getpass() 
token = raw_input('Input token:')

def send_message(token):
    msg = raw_input('Input your message:')
    params = {"msg":msg,
              "token" :token,
            }
    response = requests.post(URL_LiSTENER, data=params)
    print response.text

def get_user_msgs(login, password, token):
    params = {"login":login,
              "pass":password,
              "token" :token,
            }
    response = requests.post(URL_ND, data=params)
    try:
        dict_of_msgs=json.loads(response.text)
        numbers = dict_of_msgs.keys()
        numbers.sort()
        for number in numbers:
            print number,".",dict_of_msgs[number]
    except ValueError:
        print response.text

def func_for_daemon():
    while 1:
        print getStatus()
        sleep(5)

if __name__ == "__main__":
    if args.foreground:
         daemon = Daemonize(app="test_app", pid=PID_FILE, action=func_for_daemon())
         daemon.start()
    if args.send_msg:
        send_message(token)
    else:
        get_user_msgs(login, password, token)        
