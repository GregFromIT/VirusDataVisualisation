#helpful stuff
from math import gamma
import time
import random

#imports data processing
import numpy as np
from numpy import zeros 
import scipy as sp
from scipy.integrate import odeint

#import visualisations
import matplotlib.animation as anim
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation  

#importing GUI 
# import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


# def SIRModel1():
    # beta = 10/(40*8*24)
    # gamma = 3/(15*24)
    # dt = 0.1
    # Da = 30
    # N_t = int(Da*24/dt)

    # t = np.linspace(0, N_t*dt, N_t+1)
    # Sa = zeros(N_t+1)
    # Ia = zeros(N_t+1)
    # Ra = zeros(N_t+1)

    # Sa[0] = 5000
    # Ia[0] = 1
    # Ra[0] = 0

    # for n in range(N_t):
    #     Sa[n+1] = Sa[n] - dt*beta*Sa[n]*Ia[n]
    #     Ia[n+1] = Ia[n] + dt*beta*Sa[n]*Ia[n] - dt*gamma*Ia[n]
    #     Ra[n+1] = Ra[n] + dt*gamma*Ia[n]
        
    # fig = plt.figure()
    # l1, l2, l3 = plt.plot(t, Sa, t, Ia, t, Ra)
    # fig.legend((l1, l2, l3), ('S', 'I', 'R'), 'upper left')
    # plt.xlabel('hours')
    # plt.draw()
    # plt.show()

# populationSize = 1*10**6
# Infected = 10
# Recovered = 0
# Susceptible = populationSize - Infected
# InfectedPercent = (Infected/populationSize) *100
# RecoveredPercent = (Recovered/populationSize) *100
# SusceptiblePercent = (Susceptible/populationSize) *100



N = 1
I0, R0 = 1, 0 
S0 = N - I0 - R0
days = 100
beta, gamma0 = 0.2, (1./days)
t = np.linspace(0, 160, 160)

def SIRModel():
    def deriv(y,t,N,beta,gamma):
        S, I, R = y
        dSdt = -beta *S*I/N
        dIdt = beta * S * I/N - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt    
    
    y0 = S0, I0, R0

    ret = odeint(deriv, y0, t, args=(N, beta, gamma0))
    S, I, R = ret.T 

    fig = plt.figure(facecolor="w")
    ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)      
    ax.plot(t, S/100, 'b', alpha=0.5, lw=2, label='Susceptible')
    ax.plot(t, I/100, 'r', alpha=0.5, lw=2, label='Infected')
    ax.plot(t, R/100, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
    ax.set_xlabel('Time /days')
    ax.set_ylabel('Number (1000s)')
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    for spine in ('top', 'right', 'bottom', 'left'):
        ax.spines[spine].set_visible(False)
    plt.show()   

window = Tk()

window.title("SIR Simulation")

window.geometry('1024x576')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

btn = Button(window, text="Click Me", command=SIRModel)

btn.grid(column=1, row=0)
popw1 = Scale(window, from_=0, to=200, orient="horizontal")
popw1.grid(column=1, row=1)
infectedw2 = Scale(window, from_=0, to=200, orient="horizontal")
infectedw2.grid(column=1, row=2)

N = popw1.get()
I0, R0 = infectedw2.get(), 0 
S0 = N - I0 - R0
days = 100
beta, gamma0 = 0.2, (1./days)
t = np.linspace(0, 160, 160)


window.mainloop()
