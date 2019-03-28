#!python3

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt



# x = np.linspace(0, 10, 100)
# fig = plt.figure()
# plt.subplot(2, 1, 1)
# plt.plot(x, np.sin(x), '-')
# plt.subplot(2, 1, 2)
# plt.plot(x, np.sin(x), '-')
# plt.plot(x, np.cos(x), '--')
# plt.show()


# fig = plt.figure()
# ax = plt.axes()
# x = np.linspace(0, 10, 100)
# ax.plot(x, np.sin(x))
# plt.show()



# x = np.linspace(0, 10, 100)
# fig = plt.figure()
# plt.style.use('seaborn-whitegrid')
# plt.plot(x, np.sin(x - 0), color='blue')
# plt.plot(x, np.sin(x - 1), color='g')
# plt.plot(x, np.sin(x - 2), color='0.75')
# plt.plot(x, np.sin(x - 3), color='#FFDD44')
# plt.plot(x, np.sin(x - 4), color=(1.0, 0.2, 0.3))
# plt.plot(x, np.sin(x - 5), color='chartreuse')
# plt.plot(x, x + 0, linestyle='solid')
# plt.plot(x, x + 1, linestyle='dashed')
# plt.plot(x, x + 2, linestyle='dashdot')
# plt.plot(x, x + 3, linestyle='dotted')
# # plt.plot(x, x + 4, '-')
# # plt.plot(x, x + 5, '__')
# # plt.plot(x, x + 6, '_.')
# plt.plot(x, x + 7, linestyle=':')
# plt.xlim(0, )
# plt.ylim(-1, )
# plt.show()


# x = np.linspace(0, 10, 30)
# y = np.sin(x)
# plt.plot(x, y, 'o', color='black')
# plt.show()

plt.plot(1, 1, 'o', 'marker="o"'.format('o'))
plt.plot(1, 2, 'x', 'marker="x"'.format('o'))
plt.plot(2, 1, '+', 'marker="+"'.format('o'))
plt.plot(2, 2, 'v', 'marker="v"'.format('o'))
plt.legend(numpoints=1)
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.show()

# rng = np.random.RandomState(0)
# for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
#     plt.plot(rng.rand(5), rng.rand(5), marker, label="marker='{0}'".format(marker))
#     plt.legend(numpoints=1)
#     plt.xlim(0, 1.8)
# plt.show()


