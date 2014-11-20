import unittest
from client_daemon import getstatus
from client_daemon import getUserData

class test_Client_Daemon(unittest.TestCase):

    def test_status(self):
        status = getstatus()
        response = '<Response [200]>'
        self.assertTrue(status, response)

    def userdata(self):
        mylist = []
        content = getUserData()
        mylist.append(content)
        if 'body' in mylist:
            m = True
        print mylist
        self.assertTrue(m, True)

    def pid_file():
        #check if pid file exists
        pass

if __name__ == '__main__':
    unittest.main()

