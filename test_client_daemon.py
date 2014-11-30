import unittest
from client_daemon import getStatus
from client_daemon import getUserData
from client_daemon import mytest


class test_Client_Daemon(unittest.TestCase):

    def test_status(self):
        status = getStatus()
        response = '200'
        self.assertTrue(status, response)

    def test_getUserData(self):
        mylist = []
        content = getUserData()
        mylist.append(content)
        if len(mylist) > 0 :
            length = True
        self.assertTrue(length, True)

    def pid_file(self):
        test()
        if os.path.isfile("/tmp/test.pid"):
            final = True
        self.assertTrue(final, True)

if __name__ == '__main__':
    unittest.main()

