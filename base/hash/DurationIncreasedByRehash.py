import numpy as np
import matplotlib.pyplot as plt
if __name__=='__main__':
    # x y data from output of com/refinitiv/edp/cnm/ccd/permId/PermIDCompareAndPerformanceTest.java increasedDurationByRehash

    # x = np.array([1, 5, 11, 13, 24])
    # y = np.array([181, 25136, 65550, 1965411])

    plt.title("rehash duration increased by rehash times")
    plt.xlabel("rehash times")
    plt.ylabel("rehash duration")


    # plt.plot([181, 25136, 65550, 1965411], [1, 3, 5, 10]) #1000*1000*10 times
    # plt.axis([0, 2000000, 0, 15])
    plt.plot([35, 76614], [1, 6]) #1000*1000 times
    plt.axis([0, 80000, 0, 8])



    plt.show()