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

peopleDictionary = []

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
             
def initateSim():
    popultaionSize = int(input("Pops?:"))
    startingImmunity = int(input("How Many pops are immune at start:"))
    startingInfectors = int(input("How many infected Pops"))
    for x in range(0,popultaionSize):
          peopleDictionary.append(Person(startingImmunity))
    for x in range(0,startingInfectors):
        peopleDictionary[random.randint(0,len(peopleDictionary)-1)].contagiousness = int((norm.rvs(size=1,loc=0.5,scale=0.15)[0]*10).round(0)*10)
    daysContagious = int(input("How many days contagious: "))
    lockdownDay = int(input("Day for lockdown to be enforced: "))
    maskDay = int(input("Day for masks to be used: "))
    return daysContagious, lockdownDay, maskDay      
def runDay(daysContagious, lockdown):
    for person in [person for person in peopleDictionary if person.contagiousness>0 and person.friends>0]:
        peopleCouldMeetToday = int(person.friends/2)
        if peopleCouldMeetToday > 0:
            peopleMetToday = random.randint(0,peopleCouldMeetToday)
        else:
            peopleMetToday = 0
            
        if lockdown == True:
            peopleMetToday= 0
        
        for x in range(0, peopleMetToday):
            friendInQuestion = peopleDictionary[random.randint(0,len(peopleDictionary)-1)]
            if random.randint(0,100) < person.contagiousness and friendInQuestion.contagiousness == 0 and friendInQuestion.immunity == False:
                friendInQuestion.contagiousness = int((norm.rvs(size=1,loc=0.5,scale=0.15)[0]*10).round(0)*10)
                print(peopleDictionary.index(person), " >>> ", peopleDictionary.index(friendInQuestion))
                
        for person in [person for person in peopleDictionary if person.contagiousness>0]:
            person.contagiousDays += 1
        if person.contagiousDays > daysContagious:
            person.immunity = True
            person.contagiousness = 0
            print("|||", peopleDictionary.index(person), " |||")
            
lockdown = False
daysContagious, lockdownDay, maskDay = initateSim()
saveFile = open("pandemicsave3.txt", "a")
for x in range(0,100):
    if x==lockdownDay:
        lockdown = True
        
    if x == maskDay:
        for person in peopleDictionary:
            person.wearMask()
            
    print("DAY ", x)
    runDay(daysContagious,lockdown)
    write = str(len([person for person in peopleDictionary if person.contagiousness>0])) + "\n"
    saveFile.write(write)
    print(len([person for person in peopleDictionary if person.contagiousness>0]), " people are contagious on this day.")
saveFile.close()
#Defining the variables
# populationSize = 1*10**6
# Infected = 10
# Recovered = 0
# Susceptible = populationSize - Infected
# InfectedPercent = (Infected/populationSize) *100
# RecoveredPercent = (Recovered/populationSize) *100
# SusceptiblePercent = (Susceptible/populationSize) *100
