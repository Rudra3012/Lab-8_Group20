import pytest
import json
import requests

from login_module import LoginPage

    
def test_login1():
    response = LoginPage({'username': 'Ruchir17', 'pass': 'ruchir123'})
    assert response['message'] == 'Login Unsuccessful'

def test_login():
    response = LoginPage({'username': 'Ruchir17', 'pass': 'Ruchir123'})
    assert response['message'] == 'Login Unsuccessful'

