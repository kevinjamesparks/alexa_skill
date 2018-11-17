import math
import requests
from requests_oauthlib import OAuth1
from .credentials import API_KEY

city='2950159' #berlin
base_url='http://api.openweathermap.org/data/2.5/weather'

def get_current_temp():
    """
    This functions returns the current temperature in Berlin in degC
    :return: Temperature in Berlin in degree C
    """
    params = {'id': city, 'APPID': API_KEY}
    r = requests.get(base_url, params=params)
    data = r.json()
    return math.floor(data['main']['temp'] - 273.15)
