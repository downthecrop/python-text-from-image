
# Open a file
data = open("Ubuntu-Nvidia.txt", "r")
count = len(data.readlines())
data = open("Ubuntu-Nvidia.txt", "r")

i = 0
total = 0
fpsList = []
onePercent = int(count*.01)
onePercentVal = 0

while i < count:
    fpsVal = data.readline().strip()
    print(fpsVal)
    total += int(fpsVal)
    fpsList.append(fpsVal)
    i += 1

#find onePercent lows

i = 0

while i < onePercent:
    print("Lowest Value: "+str(min(fpsList)))
    onePercentVal += int(fpsList.pop(fpsList.index(min(fpsList))))
    print(onePercentVal)
    i += 1 


print("Average:"+str(int(total/count)))
print("One percent low:"+str(int(onePercentVal/onePercent)))

## Windows NVIDIA Average: 154
## Windows NVIDIA One Percent Low: 120
##
## Ubuntu NVIDIA Average: 140
## Ubuntu NVIDIA One Percent Low: 106