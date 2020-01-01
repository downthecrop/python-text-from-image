import time
# Open a file
winData = open("Windows-Nvidia.txt", "r")
count = len(winData.readlines())
winData = open("Windows-Nvidia.txt", "r")
ubuntuData = open("Ubuntu-Nvidia.txt", "r")


i = 0

print("Starting")
time.sleep(2)

while i < count:
    print(winData.readline().strip()+"              "+ubuntuData.readline().strip())
    time.sleep(1)
    i += 1

print("Done!")