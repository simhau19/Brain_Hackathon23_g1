import requests

url = 'https://g1.cioty.com/test1'

headers = {
    "Content-Type":"application/x-www-form-urlencoded",
    "Synx-Cat":"4"
}


data = {
    'token': 'aToken_36d8715e3531fd8e8c01fcbfd26bf5af1908e14f15014d2d14817b568bc0bb0e',
    'objectID': '1',
}

with requests.post(url, headers=headers, data=data, stream=True) as response:
    for line in response.iter_lines():
        if line:
            print(line.decode('utf-8'))