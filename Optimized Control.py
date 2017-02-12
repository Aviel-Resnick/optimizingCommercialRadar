import threading
import time
import re

#   Timer starts for calculating execution time
total_time = time.time()

data_file = open("Output.txt", "r")
data = data_file.readlines()
data_file.close()

l = []
Empty = []
Objects = []
obj_count = 0
obj_ranges = 0

def read():
	global data

	data_file = open("Output.txt", "r")
	data = data_file.readlines()
	data_file.close()

def separate():
	global l
	pattern = re.compile("^\s+|\s*,\s*|\s+$")
	l = [x for x in pattern.split(str(data)) if x]
	l.remove("['")
	l.remove("']")

def analzye():
	for i in l:
		if "F" in i:
			Empty.append(str(i).replace("F",""))

		else:
			Objects.append(str(i).replace("T",""))

def result():
	global obj_count
	global obj_ranges

	if len(Objects) > 1:
		obj_count = obj_count + 1

	for i in range (0, len(Objects)-1):
		if int(Objects[int(i)+1]) - int(Objects[int(i)]) > 1:
			obj_count = obj_count + 1
			obj_ranges = str(Objects[i-13] + " - " + Objects[i] + " and " + Objects[i+1] + " - " + Objects[i+32]) 


#   Thread Definition
thread1 = threading.Thread(target=read)
thread2 = threading.Thread(target=separate)
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

print("Objects:", obj_count)
print("Ranges:", obj_ranges)
print("\n")

print("Execution Time:", time.time() - total_time)