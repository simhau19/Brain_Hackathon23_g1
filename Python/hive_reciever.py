
import os

domain = 'g1'
service = 'test1'
token = 'aToken_36d8715e3531fd8e8c01fcbfd26bf5af1908e14f15014d2d14817b568bc0bb0e'

objectID = '2'
format = 'json'

url = fr"https://{domain}.cioty.com/{service}"

os.system(f"curl -k {url} -H 'Synx-Cat: 4' -d 'token={token}&objectID={objectID}&format={format}'")
