import requests
import logging
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv('REST_URL')

def getNextRequest(dates, cnt=1):
    data = {
        'dates': dates,
        'cnt': cnt
    }
    req = requests.post(f'{URL}/rpc/get_request', json=data)
    result = req.json()
    return result

def sendResult(id, result, info):
    data = {
        'status': result,
        'info': info
    }
    headers = {
        'Prefer': 'return=representation'
    }
    req = requests.patch(f'{URL}/users?id=eq.{id}', json=data, headers=headers)
    result = req.json()
    logging.info(f'Saved {id} data: {data}')
    return result


def setSuccess(id, info):
    return sendResult(id, 'success', info)

def setFail(id, info):
    return sendResult(id, 'fail', info)