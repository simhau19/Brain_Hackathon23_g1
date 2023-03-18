

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
        'heartbeat': randint(60, 80)
    }
    print(f"Heartbeat: {data['heartbeat']}")
    result = requests.post(url, headers=headers, data=data)
    print(result.url)


while True:
    heartbeat()
    sleep(1)