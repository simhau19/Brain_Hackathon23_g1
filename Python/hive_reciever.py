
import requests
from threading import Thread
from recieve_thread import RecieveData
from multiprocessing import Queue


queue = Queue()
service1 = 'medicase'
service2 = 'medicase2'

thread1 = RecieveData(service1, queue)
thread2 = RecieveData(service2, queue)

thread1.start()
thread2.start()

while True:
    print(queue.get())



# prev_line = ""
# with requests.post(url, headers=headers, data=data, stream=True) as response:
#     for line in response.iter_lines():
#         if line:
#             print(line.decode('utf-8'))
