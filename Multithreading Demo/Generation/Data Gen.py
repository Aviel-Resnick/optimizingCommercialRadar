import random

raw_file = open("Raw_Data.txt", "w")

for i in range (1,1000001):
	num = random.randint(1,100)
	raw_file.write(str(num) + "\n")