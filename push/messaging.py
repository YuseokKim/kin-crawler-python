import argparse
import json
import os

import requests
from oauth2client.service_account import ServiceAccountCredentials

PROJECT_ID = 'kinscheduler-123'
BASE_URL = 'https://fcm.googleapis.com'
FCM_ENDPOINT = 'v1/projects/' + PROJECT_ID + '/messages:send'
FCM_URL = BASE_URL + '/' + FCM_ENDPOINT
SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']

def _get_access_token():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    credentials = ServiceAccountCredentials.from_json_keyfile_name(BASE_DIR + '/kinscheduler-123.json', SCOPES)
    access_token_info = credentials.get_access_token()
    return access_token_info.access_token

def _send_fcm_message(fcm_message):
    headers ={
        'Authorization': 'Bearer '+ _get_access_token(),
        'Content-Type': 'applicatioin/json; UTF-8',
    }

    resp = requests.post(FCM_URL, data=json.dumps(fcm_message), headers=headers)

    if resp.status_code==200:
        print('Message sent to Firebase for delivery, response:')
    else:
        print('Unable to send Message to Firebase')

def _build_message(type, title, body, link, token):
    return {
        'message': {
            'notification': {
                'title': title,
                'body': body
            },
            "data": {
                "link": link,
                'type': type
            },
            "token": token
        }

    }