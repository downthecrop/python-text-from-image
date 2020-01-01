import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.animation import FuncAnimation

plt.style.use('dark_background')
mpl.rcParams['figure.dpi'] = 300


i = 0
x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv('windows-ubuntu.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
    mpl.rcParams['lines.linewidth'] = 3
    plt.cla()

    plt.plot(x, y1, color='#0078d7', label='Windows 10 1809')
    plt.plot(x, y2, color='#e95420', label='Ubuntu 18.04 LTS')

    plt.legend(loc='lower left')
    plt.ylim((100, 241))   # set the ylim to bottom, top
    plt.xlim(left=max(0, i-50), right=i+10)
    plt.tight_layout()
    i += 1


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()