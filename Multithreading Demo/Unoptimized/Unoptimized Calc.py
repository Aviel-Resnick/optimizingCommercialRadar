# Unoptimized large numerical calculations
# PJAS 2016-2017
# Aviel Resnick

import time
import random
import subprocess

#	Timer starts for calculating execution time
total_time = time.time()

result = 1

#	Accessing the data file
with open("/home/avilor/Desktop/PJAS/PJAS 2016-2017/Multithreading Demo/Generation/Raw_Data.txt") as f:
    content = f.readlines()

#	0-250,000
def First():
	global result
	for i in range(0,250001):
		result = result * int(content[i])

#	250,000-500,000
def Second():
	global result
	for i in range(250001,500001):
		result = result * int(content[i])

#	500,000-750,000
def Third():
	global result
	for i in range(500001,750001):
		result = result * int(content[i])

#	750,000-1,000,000
def Fourth():
	global result
	for i in range(751000,1000001):
		result = result * int(content[i-1])

#	Function Calls
First()
Second()
Third()
Fourth()

print(result)
print("Execution Time:", time.time() - total_time)