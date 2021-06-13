import requests
from .endpoints import REQUEST_PATHS
from .models.status import *


def get_county_list():
    """Returns the list of valid counties"""
    request = REQUEST_PATHS['county_list']
    response = requests.get(request)
    response.raise_for_status()
    return response.json()


def get_entry_from_until(date_1, date_2):
    """Returns the updates for a specific range of dates"""
    request = REQUEST_PATHS['entry_from_until'].format(date_1=date_1, date_2=date_2)
    response = requests.get(request)
    response.raise_for_status()
    return response


def get_entry(date):
    """Returns the update of a specific date"""
    request = REQUEST_PATHS['entry'].format(date=date)
    response = requests.get(request)
    response.raise_for_status()
    return response


def get_entry_counties(date_1, date_2):
    """Returns the updates for a specific range of dates for the counties dataset"""
    request = REQUEST_PATHS['entry_counties'].format(date_1=date_1, date_2=date_2)
    response = requests.get(request)
    response.raise_for_status()
    return response


def get_entry_county(date_1, date_2, county):
    """Returns the updates for a specific range of dates for the counties dataset"""
    request = REQUEST_PATHS['entry_county'].format(date_1=date_1, date_2=date_2, county=county)
    response = requests.get(request)
    response.raise_for_status()
    return response


def get_full_dataset():
    """Returns the full dataset in a JSON format"""
    request = REQUEST_PATHS['full_dataset']
    response = requests.get(request)
    response.raise_for_status()
    return response


def get_full_dataset_counties():
    """Returns the full dataset in a JSON format for the counties"""
    request = REQUEST_PATHS['full_dataset_counties']
    response = requests.get(request)
    response.raise_for_status()
    return response


def get_last_update():
    """Returns the last updated entry"""
    request = REQUEST_PATHS['last_update']
    response = requests.get(request)
    response.raise_for_status()
    return response


def get_last_update_counties():
    """Returns the last updated entry for all counties"""
    request = REQUEST_PATHS['last_update_counties']
    response = requests.get(request)
    response.raise_for_status()
    return response


def get_last_update_specific_county(county):
    """Returns the last updated entry for a specific county"""
    request = REQUEST_PATHS['last_update_specific_county'].format(county=county)
    response = requests.get(request)
    response.raise_for_status()
    return response


def get_status():
    """Returns the status of the API"""
    request = REQUEST_PATHS['status']
    response = requests.get(request)
    response.raise_for_status()
    return Status(response.status_code, response.json()['status'])
