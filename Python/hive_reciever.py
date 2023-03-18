
import requests

domain = 'g1'
service = 'heartbeat'
token = 'aToken_36d8715e3531fd8e8c01fcbfd26bf5af1908e14f15014d2d14817b568bc0bb0e'

objectID = '1'
format = 'json'

url = fr"https://{domain}.cioty.com/{service}"

headers = {
    "Content-Type":"application/x-www-form-urlencoded",
    "Synx-Cat":"4"
}

data = {
    'token': token,
    'objectID': objectID,
    'format': format
}

with requests.post(url, headers=headers, data=data, stream=True) as response:
    print(response.headers)
    for line in response.iter_lines():
        if line:
            print(line.decode('utf-8'))
