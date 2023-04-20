import json
from pymongo import MongoClient

client = MongoClient('mongodb+srv://Group20:Group20@cluster0.fi05hgc.mongodb.net/test')
db = client['CrossWordManagement']

def LoginPage(request):
    username =request['username']
    pass1 = request['pass']

    if 4 < len(username) < 15:
        for i in username:
            if i == ' ':
                return {'message': 'Login Unsuccessful'}
    else:
        return {'message': 'Login Unsuccessful'}

    if 8 < len(pass1) < 24:
        upperCase = False
        lowerCase = False
        number = False
        special = False

        for i in pass1:
            if i == ' ':
                return {'message': 'Login Unsuccessful'}
            
            if i.isupper():
                upperCase = True
            if i.islower():
                lowerCase = True
            if i.isdigit():
                number = True
            if i in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|',
                        ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']:
                special = True
        if upperCase and lowerCase and number and special:
            pass
        else:
            return {'message': 'Login Unsuccessful'}
    else:
        return {'message': 'Login Unsuccessful'}

    collections = db['crosswordApp_user']
    reply = collections.find_one({"username": username})

    # if username is not in database
    if reply is None:
        return {'message': 'Login Unsuccessful'}

    return {'message': 'Login Successful'}
