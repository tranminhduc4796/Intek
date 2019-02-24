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
    credentials = flow.run_local_server()
    return credentials.token


def save_file(file, response):
    with open(file, 'w+') as f:
            f.write(response.text)


def request(method, url, params=None, headers=None,
                body=None, file=None, response_file=None):
    dic = {
           "get": requests.get,
           "post": requests.post,
           "put": requests.post,
           "delete": requests.delete
          }
    request_operation = dic.get(method, None)
    if request_operation:
        if method == "get":
            response = request_operation(url, params=params, headers=headers)
        elif not file:
            response = request_operation(url, params=params, headers=headers,
                                     json=body)
        else:
            response = request_operation(url, params=params, headers=headers,
                                     json=body, files=file)
        if response_file:
            save_file(response_file, response)
    return response


if __name__ == "__main__":
    scope = ['https://www.googleapis.com/auth/youtube',
             'https://www.googleapis.com/auth/youtube.force-ssl']
    client_secret_file = 'client_secret.json'
    info = read_config()
    credentials = get_credential_token()
    # For authentication
    info['headers']['Authorization'] = 'Bearer {}'.format(credentials)
    response = request(info['method'],
                       info['url'],
                       params=info['param'],
                       headers=info['headers'],
                       body=info['body'],
                       file=info['file'],
                       response_file='response')
    data = dump.dump_all(response)
    print('Data:\n', data.decode('utf-8'))
