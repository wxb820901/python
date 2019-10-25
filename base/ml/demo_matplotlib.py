#!python3

import numpy as np
import matplotlib.pyplot as plt


def show(x, y):
    plt.plot(x, y)
    plt.show()


def show2(x, y1, y2):
    plt.plot(x, y1, 'ro', x, y2, 'g--')
    plt.show()


def show_sub2(x, y1, y2):
    plt.subplot(211)
    plt.plot(x, y1)
    plt.subplot(212)
    plt.plot(x, y2)
    plt.show()


def show_sub3(x, y1, y2, y3):
    plt.subplot(311)
    plt.plot(x, y1)
    plt.subplot(312)
    plt.plot(x, y2)
    plt.subplot(313)
    plt.plot(x, y3)
    plt.show()


if __name__ == '__main__':
    x = np.linspace(-10, +10)

    func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))  # np.poly1d 创建多项式
    func_deriv1 = func.deriv(m=1)  # 1阶导数
    func_deriv2 = func.deriv(m=2)  # 1阶导数

    y = func(x)
    y_deriv1 = func_deriv1(x)
    y_deriv2 = func_deriv2(x)

    # show(x, y_deriv1)
    # s2(x, y, y_deriv)
    # show_sub2(x, y, y_deriv)
    show_sub3(x, y, y_deriv1, y_deriv2)
