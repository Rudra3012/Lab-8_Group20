import pytest
import json
import requests

from login_module import LoginPage

    
def test_login1():
    response = LoginPage({'username': 'Ruchir17', 'pass': 'ruchir123'})
    assert response['message'] == 'Login Unsuccessful'

def test_login2():
    response = LoginPage({'username': 'Ruchir17', 'pass': 'Ruchir123'})
    assert response['message'] == 'Login Unsuccessful'

def test_login3():
    response = LoginPage({'username': 'Ruchir17', 'pass': 'Ru@123'})
    assert response['message'] == 'Login Unsuccessful'

def test_login4():
    response = LoginPage({'username': 'Ruchir17', 'pass': 'Ruchir12345678998948974987984'})
    assert response['message'] == 'Login Unsuccessful'

def test_login5():
    response = LoginPage({'username': 'Ruchir17', 'pass': 'Ruchir@123'})
    assert response['message'] == 'Login Successful'

