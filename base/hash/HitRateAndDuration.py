import numpy as np
import matplotlib.pyplot as plt
if __name__=='__main__':
    # assume that 1 time of hash is a unit action, it means duration is the same
    #   consider the feature what effect hash, is just the string length. and for rehash the string is almostly same
    # assume 2

    x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    y = x

    plt.title("perm id range token and max rehash duration")
    plt.xlabel("perm id range token")
    plt.ylabel("max rehash duration")
    plt.plot(x, y)
    plt.show()