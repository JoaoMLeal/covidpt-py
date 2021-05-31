import requests
from .endpoints import REQUEST_PATHS
from .models.status import *
from .utils import today, yesterday


def get_status():
    request = REQUEST_PATHS['status']
    response = requests.get(request)
    return Status(response.status_code, response.json()['status'])


def get_entry(date):
    request = REQUEST_PATHS['entry'].format(date=date)
    response = requests.get(request)


def get_entry_today():
    return get_entry(today())

