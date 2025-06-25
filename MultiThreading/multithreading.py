import threading
import time

def function():
    for _ in range(100):
        print("Thread 1 is running\n")
    # Simulate some work
    
def function1():
    for _ in range(100):
        print("Thread2 is running\n")
    # Simulate some work
def function2():
    for _ in range(100):
        print("Thread 3 is running\n")
    # Simulate some work

# Create threads
thread1 = threading.Thread(target=function,)
thread2 = threading.Thread(target=function1,)
thread3 = threading.Thread(target=function2,)
# thread3 = threading.Thread(target=function,)
# Start threads
thread1.start()
thread2.start()
thread3.start()
# Wait for all threads to complete
thread1.join()
thread2.join()
thread3.join()
print("All threads have completed")
print("Main thread is exiting")