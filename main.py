#helpful stuff
import time
import math
import random

#imports data processing
import pandas as pd
import numpy as np
import scipy as sp
from scipy.stats import norm

#import visualisations
import matplotlib.animation as anim
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

#create person class
class Person():
    def __init__(self, startingImmunity):
        if random.randint(0,100) < startingImmunity:
            self.immunity = True
        else:
            self.immunity = False
        #initalisating other variables
        self.contagiousness = 0
        self.mask = False
        self.contagiousDays = 0
        self.friends = int((norm.rvs(size=1,loc=0.5,scale=0.15)[0]*10).round(0))
    def wearMask(self):
        self.contagiousness /= 2       
             
        



#Defining the variables
populationSize = 1*10**6
Infected = 10
Recovered = 0
Susceptible = populationSize - Infected
InfectedPercent = (Infected/populationSize) *100
RecoveredPercent = (Recovered/populationSize) *100
SusceptiblePercent = (Susceptible/populationSize) *100
