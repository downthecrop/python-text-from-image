
# Open a file
in_file = "Windows11.hml_out.txt"
data = open(in_file, "r")
count = len(data.readlines())
data = open(in_file, "r")

i = 0
total = 0
fpsList = []
onePercent = int(count*.01)
onePercentVal = 0

while i < count:
    fpsVal = data.readline().strip()
    fpsVal = fpsVal.split('.')
    fpsVal = fpsVal[0]
    #print(fpsVal)
    total += int(fpsVal)
    fpsList.append(fpsVal)
    i += 1

#find onePercent lows

i = 0

while i < onePercent:
    #print("Lowest Value: "+str(min(fpsList)))
    onePercentVal += int(fpsList.pop(fpsList.index(min(fpsList))))
    #print(onePercentVal)
    i += 1 

print(in_file)
print("Average:"+str(int(total/count)))
print("One percent low:"+str(int(onePercentVal/onePercent)))

## Windows NVIDIA Average: 154
## Windows NVIDIA One Percent Low: 120
##
## Ubuntu NVIDIA Average: 140
## Ubuntu NVIDIA One Percent Low: 106