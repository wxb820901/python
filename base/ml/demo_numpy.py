#!python3

import numpy as np


def pa(label, s):
    print(label + '\n' + str(s) + "\n------------------------------------------")


if __name__ == '__main__':
    pa('np.array([1, 2, 3])', np.array([1, 2, 3]))
    pa('np.array([[1, 2], [3, 4]])', np.array([[1, 2], [3, 4]]))
    pa('np.array([1, 2, 3, 4, 5, 6], ndmin=2)', np.array([1, 2, 3, 4, 5, 6], ndmin=2))
    pa('np.array([1, 2, 3], dtype=complex)', np.array([1, 2, 3], dtype=complex))
    pa('np.array([1, 2, 3], dtype=\'float32\')', np.array([1, 2, 3], dtype='float32'))

    pa('np.array(list(range(10)))', np.array(list(range(10))))
    pa('[str(c) for c in list(range(10))]', [str(c) for c in list(range(10))])
    pa('[type(item) for item in [True, "2", 3.0, 4]]', [type(item) for item in [True, "2", 3.0, 4]])
    pa('np.array([range(i, i + 3) for i in [2, 4, 6]])', np.array([range(i, i + 3) for i in [2, 4, 6]]))

    pa('np.zeros(10, dtype=int)', np.zeros(10, dtype=int))
    pa('np.zeros((3, 3), dtype=int)', np.zeros((3, 3), dtype=int))
    pa('np.ones((3, 5), dtype=int)', np.ones((3, 5), dtype=int))
    pa('np.full((3, 5), 17)', np.full((3, 5), 17))
    pa('np.arange(0, 20, 2)', np.arange(0, 20, 2))
    pa('np.linspace(0, 1, 6)', np.linspace(0, 1, 6))
    pa('np.linspace(0, 1, 5)', np.linspace(0, 1, 5))
    pa('np.linspace(0, 1, 7)', np.linspace(0, 1, 7))
    pa('np.random.random((3, 3)))', np.random.random((3, 3)))  # 3*3 0-1 均匀分布的随机数
    pa('np.random.normal(0, 1, (3, 3))', np.random.normal(0, 1, (3, 3)))  # 3*3 均值为0， 方差为1，正态分布的随机数
    pa('np.random.randint(0, 10, (3, 3))', np.random.randint(0, 10, (3, 3))) # 0到10之间，随机整数
    pa('', np.eye(3)) # 单位矩阵
    pa('', True)
    pa('', True)
    pa('', True)
    pa('', True)
    pa('', True)
    pa('', True)
    pa('', True)
    pa('', True)
