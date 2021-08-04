import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.animation import FuncAnimation

F1 = "Windows10.hml_out.txt"
F2 = "Windows11.hml_out.txt"
OUT = "out.csv"

def animate(i):
    data = pd.read_csv(OUT)
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
    mpl.rcParams['lines.linewidth'] = 3
    plt.cla()

    plt.plot(x, y1, color='#0078d7', label='Windows 10 1809')
    plt.plot(x, y2, color='#d7003d', label='Windows 11 21H2')
    if i >= 10:
        print(F1_data.readline().strip()+"              "+F2_data.readline().strip())
    plt.legend(loc='lower left')
    plt.ylim((100, 241))   # set the ylim to bottom, top
    plt.xlim(left=max(0, i-50), right=i+10)
    plt.tight_layout()
    i += 1

F1_data = open(F1, "r")
F2_data = open(F2, "r")
count = len(F2_data.readlines())
F2_data = open(F2, "r")
combined = open(OUT,"w+")

#Header of CSV
combined.write("x_value,total_1,total_2"+"\n\n")

i = 0
while i < count+20:
    if i < 20:
        # Junk data so the graph doesn't start right away
        combined.write(str(i)+",0,0"+"\n\n")
    else:
        F1_line = F1_data.readline()
        F2_line = F2_data.readline()
        combined.write(str(i)+","+str(F1_line).rstrip('\r\n')+","+str(F2_line)+"\n\n")
    i += 1
combined.close()

i = 0

plt.style.use('dark_background')
mpl.rcParams['figure.dpi'] = 300

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()