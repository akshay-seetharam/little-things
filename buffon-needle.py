import numpy as np
import math
from matplotlib import pyplot as plt

def drop_line(grid_size=1000000):
    endpoint = (np.random.random() * grid_size, np.random.random() * grid_size)
    theta = np.random.random() * math.tau
    other_endpoint = (endpoint[0] + np.cos(theta), endpoint[1] + np.sin(theta))

    return np.floor(endpoint[0]) != np.floor(other_endpoint[0])

def main():
    runs = 1000
    intersections = 0
    rts = []
    for i in range(runs):
        if drop_line():
            intersections += 1
        rts.append(intersections / (i + 1.0))

    plt.plot(range(runs), rts)
    plt.axhline(4 / math.tau, c='RED')
    plt.show()
    print(rts)
    print(4 / rts[-1], math.tau)

if __name__ == '__main__':
    main()
