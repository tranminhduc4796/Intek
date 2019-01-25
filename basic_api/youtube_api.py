#!/usr/bin/python

import httplib2
import os
import re
import sys
import json
import requests

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow



def get_request():
    """
    Read the file config.json to get the request
    """
    request = json.load(open('config.json'))
    return request


def get_credential_token():
    """
    To use Google API, we need to have a credential token to access our app.
    Refer to below to create a credential token with enabled Youtube API:
    https://console.developers.google.com/start/api?id=youtube
    """
    flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, scope)
    credentials = flow.run_console()
    return credentials.token


if __name__ == "__main__":
    scope = ['https://www.googleapis.com/auth/youtube']
    api_service_name = 'youtube'
    api_version = 'v3'
    client_secret_file = 'client_secret.json'
    url = 'https://www.googleapis.com/youtube/v3/'
    request = get_request()
    print(request['param'])
    credential_token = get_credential_token()
    if request['method'] == 'download' or request['method'] == 'list':
        response = requests.get(url=url + request['resource'], 
                                params=request['param'],
                                headers={'Authorization': 'Bearer %s' % credential_token})
    print(response.json())

