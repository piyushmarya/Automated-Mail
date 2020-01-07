import json


data = json.load(open(r''))

def getDetails(user):
    return data[user]
