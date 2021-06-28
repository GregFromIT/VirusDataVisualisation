import pandas as pd
import math
import scipy
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import time

# x = [1,2,3]
# y= [2,4,6]
# z = [3,6,9]
# plt.plot(x,y)
# plt.plot(x,z)
# plt.plot(z,y)
# plt.title('ref title')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.draw()
# plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("sampleText.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()