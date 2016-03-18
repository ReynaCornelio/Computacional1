# -*- coding: utf-8 -*-
"""
Created on Sat Mar 05 11:04:15 2016

@author: Reyna
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

fig =plt.figure()
xA = []
yA = []
xB = []
yB = []

i = 0
while (i <= 90):
    i = i+1
    Ang = (i*np.pi)/180
    f = lambda x: 1/np.sqrt(np.cos(x)-np.cos(Ang))
    F, erri = integrate.quadrature(f, 0, Ang, maxiter=100)
    T = 4 * np.sqrt(0.8/9.8)*(1/np.sqrt(2))*F
    Ths = 2*np.pi*np.sqrt(0.8/9.8)
    T = T/Ths
    xA.append(i)
    yA.append(T)
    
    f = lambda z: 1/np.sqrt(np.cos(z)-np.cos(Ang))
    F, erri = integrate.quad(f,0,Ang)
    T = 4*np.sqrt(0.8/9.8)*(1/np.sqrt(2)*F)
    T = T/Ths
    xB.append(i)
    yB.append(T)
    
plt.plot(xA,yA, 'm')
plt.plot(xB,yB, 'b')

plt.xlabel(r'\textit{\' Desviación del valor real y la aproximació}', fontsize=10)
plt.ylabel(r'\textit{periodo }', fontsize=10)

plt.show()




