#!/usr/bin/python

# Open a file
wNv = open("Windows-Nvidia.txt", "r")
uNv = open("Ubuntu-Nvidia.txt", "r")
combined = open("windows-ubuntu.csv","w+")

count = len(wNv.readlines())

wNv = open("Windows-Nvidia.txt", "r")

i = 0

combined.write("x_value,total_1,total_2"+"\n\n")
while i < 20:
    combined.write(str(i)+",0,0"+"\n\n")
    i += 1

while i < count+20:
    wLine = wNv.readline()
    uLine = uNv.readline()
    #print("Windows: "+str(wLine))
    combined.write(str(i)+","+str(wLine).rstrip('\r\n')+","+str(uLine)+"\n\n")


    i += 1

    # Close opend file
combined.close()