import requests
import logging
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv('REST_URL')

def saveUser(user):
    headers = {
        'Prefer': 'resolution=merge-duplicates'
    }
    data = {
        'id': user.id,
        'user': {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_bot': user.is_bot,
            'username': user.username,
            'language_code': user.language_code
        }
    }
    req = requests.post(f'{URL}/rpc/save_user', json=data, headers=headers)
    if req is None:
        req = requests.get(f'{URL}/users?eq.{user.id}')
    logging.info(req.json())
    return req.json()


def saveDeclaration(user, declaration, step=None, status=None):
    headers = {
        'Prefer': 'resolution=merge-duplicates'
    }
    data = {
        'id': user.id,
        'user': {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_bot': user.is_bot,
            'username': user.username,
            'language_code': user.language_code
        },
        'request': declaration,
        'step': step,
        'status': status
    }
    logging.info(data)
    req = requests.post(f'{URL}/rpc/save_user', json=data, headers=headers)
    return req.json()    

