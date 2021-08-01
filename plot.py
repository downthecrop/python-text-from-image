import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.animation import FuncAnimation

def animate(i):
    data = pd.read_csv('windows-ubuntu.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
    mpl.rcParams['lines.linewidth'] = 3
    plt.cla()

    plt.plot(x, y1, color='#0078d7', label='Windows 10 1809')
    plt.plot(x, y2, color='#e95420', label='Ubuntu 18.04 LTS')
    if i >= 10:
        print(f1_data.readline().strip()+"              "+f2_data.readline().strip())
    plt.legend(loc='lower left')
    plt.ylim((100, 241))   # set the ylim to bottom, top
    plt.xlim(left=max(0, i-50), right=i+10)
    plt.tight_layout()
    i += 1



f1 = "Ubuntu-Nvidia.txt"
f2 = "Windows-Nvidia.txt"
out = "windows-ubuntu.csv"


f1_data = open(f1, "r")
f2_data = open(f2, "r")
count = len(f2_data.readlines())
f2_data = open(f2, "r")
combined = open(out,"w+")

#Header of CSV
combined.write("x_value,total_1,total_2"+"\n\n")

i = 0
while i < count+20:
    if i < 20:
        # Junk data so the graph doesn't start right away
        combined.write(str(i)+",0,0"+"\n\n")
    else:
        f1_line = f1_data.readline()
        f2_line = f2_data.readline()
        combined.write(str(i)+","+str(f1_line).rstrip('\r\n')+","+str(f2_line)+"\n\n")
    i += 1
combined.close()

i = 0

plt.style.use('dark_background')
mpl.rcParams['figure.dpi'] = 300

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()