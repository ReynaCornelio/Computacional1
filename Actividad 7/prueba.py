# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:19:12 2016

@author: Reyna
"""

import numpy as np
import matplotlib.pyplot as plt
import pylab as p
from scipy.integrate import odeint

def f(Y, t):
    y1, y2 = Y
    return [y2, -np.sin(y1)-0.1*y2]
f3 = plt.figure()
y1 = np.linspace(-3.14, 20.0, 10)
y2 = np.linspace(-10, 10, 10)
Y1, Y2 = np.meshgrid(y1, y2)
t = 0
u, v = np.zeros(Y1.shape), np.zeros(Y2.shape)
M = (np.hypot(u, v))
M[ M == 0] = 1. 
u /= M 
v /= M

Q = plt.quiver(Y1, Y2, u, v,cmap = 'PiYG')
NI, NJ = Y1.shape
f2 = plt.figure()
for i in range(NI):
    for j in range(NJ):
            x = Y1[i, j]
            y = Y2[i, j]
            yprime = f([x, y], t)
            u[i,j] = yprime[0]
            v[i,j] = yprime[1]

Q = plt.quiver(Y1, Y2, u, v,M, cmap = 'spring')

plt.xlabel('$y_1$')
plt.ylabel('$y_2$')
plt.xlim([-4, 16])
plt.ylim([-8, 8])
plt.savefig('EF.png')

for y20 in [-2.5,-2,-1.5,-1,-0.5, 0, 0.5, 1, 1.5, 2,2.5]:
    tspan = np.linspace(0, 50, 200)

    y0 = [0, y20]
    y1 = [np.pi, y20]
    ys = odeint(f, y0, tspan)
    ys1 = odeint(f, y1, tspan)

    plt.plot(ys[:,0], ys[:,1], 'y-')
    plt.plot(ys[:,0], -ys[:,1], 'y-')
    plt.plot(ys1[:,0], ys1[:,1], 'y-')
    plt.plot(ys1[:,0], -ys1[:,1], 'y-')
    plt.plot([ys[0,0]], [ys[0,1]], 'y')
    plt.plot([ys[-1,0]], [ys[-1,1]], 'y')

plt.xlabel(r'\textit{\'Angulo }', fontsize=16)
plt.ylabel(r'\textit{Velocidad angular }', fontsize=16)

plt.title(r'\textit{Espacio Fase}', fontsize=15)
plt.xlim([-np.pi, 5*np.pi])
plt.savefig('EF2.png')
plt.show()