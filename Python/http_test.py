import requests

url = 'https://g1.cioty.com/test1'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)

print(x.text)