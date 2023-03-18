

import os
import requests
from time import sleep
from random import randint

os.system('clear')

domain = 'g1'
token = 'aToken_36d8715e3531fd8e8c01fcbfd26bf5af1908e14f15014d2d14817b568bc0bb0e'

objectID = '1'

headers = {
    "Content-Type":"application/x-www-form-urlencoded",
    "Synx-Cat":"1"
}


def heartbeat() -> None:
    service = 'heartbeat'
    url = fr"https://{domain}.cioty.com/{service}"
    data = {
        'token': token,
        'objectID': objectID,
        'heartbeat': randint(60, 70)
    }
    print(f"Heartbeat: {data['heartbeat']} bpm")
    requests.post(url, headers=headers, data=data)


def temperature() -> None:
    service = 'temp'
    url = fr"https://{domain}.cioty.com/{service}"
    data = {
        'token': token,
        'objectID': objectID,
        'data': randint(45, 50)
    }
    print(f"Temperature: {data['data']} °C")
    requests.post(url, headers=headers, data=data)


def gps() -> None:
    service = 'gps'
    url = fr"https://{domain}.cioty.com/{service}"
    data = {
        'token': token,
        'objectID': objectID,
        'longitude': 10.40,
        'latitude': 63.41
    }
    print(f"Latitude: {data['latitude']}, Longitude: {data['longitude']}")
    requests.post(url, headers=headers, data=data)


while True:
    heartbeat()
    temperature()
    gps()
    print()
    sleep(1)