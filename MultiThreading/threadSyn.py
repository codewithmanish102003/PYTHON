import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

# threads = [threading.Thread(target=increment) for _ in range(2)]
# [t.start() for t in threads]
# [t.join() for t in threads]

threads = []

thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)
thread3 = threading.Thread(target=increment)
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
# thread1.start()
# thread2.start()
# thread3.start()
for thread in threads:
    thread.start()
    thread.join()

print("Counter:", counter)