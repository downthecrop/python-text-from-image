import csv

with open('HardwareMonitoring.hml', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        #FPS
        print(row[len(row)-1])
