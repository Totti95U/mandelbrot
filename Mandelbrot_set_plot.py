# -*- coding: utf-8 -*-
from numba import jit
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import matplotlib.animation as animation


fig = plt.figure(figsize=(7, 7))
ims = []


# time:時間(アニメーション用)，SIZE:分割量，x:描画する中心のx座標
# y:描画する中心のy座標，mag:time=0の時の描画幅の1/2
@jit('void(i4, i4, f8, f8, f8)')
def mandel_set(time, SIZE, x, y, mag):
    plt.cla()
    mag = 1/(2**time) * mag
    x_max = x + mag
    x_min = x - mag
    y_max = y + mag
    y_min = y - mag
    x = np.linspace(x_min, x_max, SIZE)
    y = np.linspace(y_min, y_max, SIZE)
    z = np.zeros((SIZE, SIZE), dtype=float)
    c = np.zeros((SIZE, SIZE), dtype=complex)
    for j in range(SIZE):
        for i in range(SIZE):
            c[i, j] = x[j] + y[i] * 1j
    z0 = 0.0 + 0.0j

    for i in range(SIZE):
        for j in range(SIZE):
            zn = z0
            for n in range(500):
                zn = zn*zn + c[i, j]
                if np.abs(zn) > 2.0:
                    z[i, j] = np.sin(n/np.pi)
                    break
                if n == 499:
                    z[i, j] = 2
                    break
    z[0, 0] = 2.0  # ここで2.0に固定しておく点が無いと色の表示がずれる

    X, Y = np.meshgrid(x, y)
    plt.contourf(X, Y, z, cmap=cm.RdGy)
    plt.show()

mandel_set(0, 500, -0.75, 0.0, 1.5)
