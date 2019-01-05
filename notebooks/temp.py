import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import json
from random import random

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xtitles = ["Paper", "Rock", "Scissors"]
x = [0, 1, 2]

def animate(i):
    y = [random(), random(), random()]

    ax.clear()
    plt.bar(x, y, align='center')
    plt.xticks(np.arange(3), xtitles)
    plt.ylim(0,1)


anim=animation.FuncAnimation(fig,animate,repeat=False,frames=50,interval=200)
plt.show()
