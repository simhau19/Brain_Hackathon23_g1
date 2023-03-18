
from threading import Thread
from multiprocessing import Queue
import requests
import json

class RecieveData(Thread):
    def __init__(self, service: str, queue: Queue) -> None:
        self.service = service
        self.queue = queue
        super().__init__(target = self.run, daemon=True)
    
    def run(self) -> None:
        domain = 'g1'
        token = 'aToken_36d8715e3531fd8e8c01fcbfd26bf5af1908e14f15014d2d14817b568bc0bb0e'

        objectID = '1'
        format = 'json'

        url = fr"https://{domain}.cioty.com/{self.service}"
        
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
            for line in response.iter_lines():
                if line:
                    self.queue.put(json.loads(line.decode('utf-8'))['RTW'])