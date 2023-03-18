
import os

os.system('clear')

domain = 'g1'
service = 'heartbeat'
token = 'aToken_36d8715e3531fd8e8c01fcbfd26bf5af1908e14f15014d2d14817b568bc0bb0e'

objectID = '1'  
tags = ['heartbeat']
data = ''

url = fr"https://{domain}.cioty.com/{service}"

format = ", ".join([f"<{tag}>" for tag in tags])
print(f"{service.upper()}\n\nWrite data here:\nFormat: {format}")

while True:
    try:
        data = input("> ").split(", ")
        result = ""
        for i, header in enumerate(tags):
            result += f"&{header}={data[i]}"
        os.system(f"curl -k {url} -H 'Synx-Cat: 1' -d 'token={token}&objectID={objectID}{result}'")
    except Exception:
        continue