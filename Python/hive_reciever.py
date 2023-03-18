import matplotlib.pyplot as plt
from recieve_thread import RecieveData
from multiprocessing import Queue


queue: Queue = Queue()
service1 = 'medicase'
service2 = 'medicase2'

thread1 = RecieveData(service1, queue)    
thread2 = RecieveData(service2, queue)

thread1.start()
thread2.start()

# Initialize the plot
fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_ylim(20, 45)
ax.set_xlabel('Time')
ax.set_ylabel('Temperature')
ax.set_title('Live Temperature Data')

# Update the plot
temperature = []
while True:
    # Get the temperature data from the queue
    result = queue.get()
    print(result)
    # For plotting
    if "TEMPERATURE" in result:
        result = result["TEMPERATURE"]
        temperature.append(float(result))
        
        # Update the plot
        x = list(range(len(temperature)))
        y = temperature
        line.set_data(x, y)
        ax.relim()
        ax.autoscale_view()
        plt.draw()
        plt.pause(0.1)  # wait for a short time before updating the plot again
