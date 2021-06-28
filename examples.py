import pandas as pd
import math
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
import matplotlib.animation as anim
from matplotlib.animation import FuncAnimation
import time
plt.style.use('seaborn-pastel')

x = [1,2,3]
y= [2,4,6]
z = [3,6,9]
plt.plot(x,y)
plt.plot(x,z)
plt.plot(z,y)
plt.title('ref title')
plt.xlabel('x')
plt.ylabel('y')
plt.draw()
plt.show()

fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,
def animate(i):
    x = np.linspace(0, 4, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,
anim = FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)
anim.save('sine_wave.gif', writer='imagemagick')