import unittest
import json
import requests

from login_module import LoginPage

class TestLogin(unittest.TestCase):
    def test_login1(self):
        response = LoginPage({'username': 'test', 'pass': 'test'})
        self.assertEqual(response['message'], 'Login Successful')
        
        
if __name__ == '__main__':
    unittest.main()
