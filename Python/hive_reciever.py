
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

