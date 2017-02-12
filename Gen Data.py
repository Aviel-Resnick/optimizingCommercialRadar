import threading
import time
#data = open("Output.txt", "r") 

#   Timer starts for calculating execution time
total_time = time.time()
def read():
    for i in range (1,10000):
        print("Reading 1")

def seperate():
    for i in range (1,10000):
        print("Seperate 2")

def analzye():
    for i in range (1,10000):
        print("Analyze 3")

def result():
    for i in range (1,10000):
        print("Result 4")
'''
read()
seperate()
analzye()
result()
'''

#   Thread Definition
thread1 = threading.Thread(target=read)
thread2 = threading.Thread(target=seperate)
thread3 = threading.Thread(target=analzye)
thread4 = threading.Thread(target=result)

#   Thread Initialization
thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

print("Execution Time:", time.time() - total_time)
