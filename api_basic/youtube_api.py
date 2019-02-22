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

from requests_toolbelt.utils import dump

def read_config():
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


def get_request(url, resource, params=None, headers=None, response_file=None):
    response = requests.get(url=url + resource, 
                            params=params,
                            headers=headers)
    if response_file:
        with open(response_file, 'w+') as f:
                f.write(response.text)
    return response

if __name__ == "__main__":
    scope = ['https://www.googleapis.com/auth/youtube']
    api_service_name = 'youtube'
    api_version = 'v3'
    client_secret_file = 'client_secret.json'
    url = 'https://www.googleapis.com/youtube/v3/'
    info = read_config()
    credential_token = get_credential_token()
    headers = info['headers']
    headers['Authorization'] = 'Bearer {}'.format(credential_token)  # For authentication
    get_method_ls = ['download', 'list', 'getRating']
    post_method_ls = ['insert', 'setModerationStatus', 'markAsSpam', 'set', 'rate', 'reportAbuse', 'unset']
    # Methods with GET HTTP method
    if info['method'] in get_method_ls:
        if info['method'] == 'getRating':
            if info['resource'] == 'videos':
                response = get_request(url, info['resource'], params=info['param'], headers=headers) 
            else:
                raise ValueError('This resource does not support this method')
        else:
            response = get_request(url, info['resource'], params=info['param'], headers=headers)
    # Methods with POST HTTP method  
    elif request['method'] in post_method_ls:


    data = dump.dump_all(response)
    print('Data:\n', data.decode('utf-8'))