import csv

in_file = "Windows11.hml"
out_file  = "_out.txt"
f= open(in_file+out_file,"w+")

if __name__ == "__main__":
    with open(in_file, newline='') as csvfile:
        
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            f.write(row[len(row)-1]+"\n")
            print(row[len(row)-1])
    f.close()
    print("Done!")