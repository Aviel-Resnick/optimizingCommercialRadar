import time

ranges = [21,22,23,24,25,26,27,28,29,30,31,32,32,33,34,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113]
text_file = open("Output.txt", "w")

#2 Objects at 21-34 and 82-113

while True:
    for i in range(1,181):
        if i not in ranges:
            print("Angle =", i)
            text = (str(i) + "F" + ",")
            text_file.write(str(text))
            time.sleep(0.02)
        else:
            print("Angle =", i, "HIT")
            text = (str(i) + "T" + ",")
            text_file.write(str(text))
            time.sleep(0.02)
            
    for i in range(-180,0):
        if abs(i) not in ranges:
            print("Angle =", abs(i))
            text_file.write(str(i))
            time.sleep(0.02)
        else:
            print("Angle =", abs(i), "HIT")
            text_file.write(str(i))
            time.sleep(0.02)