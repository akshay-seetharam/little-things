from numpy.random import random as r
import numpy as np
from matplotlib import pyplot as plt

in_sec = 0
tot = 0
approx = []

fig, axs = plt.subplots(nrows=1, ncols=2)
x = np.linspace(0, 1, 1000)
circ = [np.sqrt(1 - x**2) for x in x]
axs[0].plot(circ, x, color='orange')

rx = []
ry = []

for i in range(100000):
    rx.append(r())
    ry.append(r())

axs[0].scatter(rx, ry, alpha = 0.5)

for count, value in enumerate(rx):
    if ry[count] < np.sqrt(1 - value ** 2):
        in_sec += 1
    tot += 1
    approx.append(in_sec/tot)

approx = np.asarray(approx) * 4

axs[1].plot(range(len(approx)), approx)
axs[1].plot(np.ones(len(approx)) * np.pi)

plt.show()
