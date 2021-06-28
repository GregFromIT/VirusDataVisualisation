#helpful stuff
import time
import math
import random

#imports data processing
import pandas as pd
import numpy as np
from numpy import zeros 
import scipy as sp

#import visualisations
import matplotlib.animation as anim
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation  

beta = 10/(40*8*24)
gamma = 3/(15*24)
dt = 0.1
Da = 30
N_t = int(Da*24/dt)

t = np.linespace(0, N_t*dt, N_t+1)
Sa = zeros(N_t+1)
Ia = zeros(N_t+1)
Ra = zeros(N_t+1)

Sa[0] = 50
Ia[0] = 1
Ra[0] = 0

for n in range(N_t):
    Sa[n+1] = Sa[n] - dt*beta*Sa[n]*Ia[n]
    Ia[n+1] = Ia[n] + dt*beta*Sa[n]*Ia[n] - dt*gamma*Ia[n]
    Ra[n+1] = Ra[n] + dt*gamma*Ia[n]
    
fig = plt.figure()
l1, l2, l3 = plt.plot(t, Sa, t, Ia, t, Ra)
fig.legend((l1, l2, l3), ('S', 'I', 'R'), 'upper left')
plt.xlabel('hours')
plt.draw()
plt.show()
