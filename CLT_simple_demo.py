from time import time
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

y = []


def diceroll():
    return rd.randrange(1,7)


def coinflip():
    return rd.randrange(0,2)


def time_to_exam():
    return np.random.poisson()



def animate_clt(func):
    fig, ax = plt.subplots()
    for _ in range(200):
        x = []
        for _ in range(10):
            x.append(func())
        y.append(np.average(x))
        plt.hist(y, color='red')
        plt.title('Average: ' + str(np.average(y)))
        plt.pause(0.0001)
    plt.show()



def animate_dist(func):
    fig, ax = plt.subplots()
    for _ in range(100):
        y.append(func())
        ax.hist(y,color='red')
        plt.title('Average: ' + str(np.average(y)))
        plt.xlim(0,1)
        plt.pause(0.0001)
    print(y)
    plt.show()

animate_clt(time_to_exam)


