# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:52:21 2016

@author: Reyna
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

datos = np.loadtxt('temperaturas.txt')
x = datos[: , 0]
y = datos [: , 1]


#regresion
fitfunc = lambda p, x: p[0]*x +p[1]
#ajuste
errfunc = lambda p, x, y: fitfunc(p, x) -y

p0 = [1, 1]

#optimizando
p1,success = optimize.leastsq(errfunc, p0[:], args= (x, y))


#para graficar nuestra función

time = np.linspace(x.min(), y.max(), 100)

plt.plot(time, fitfunc(p1, time), "g-", label="Ajuste lineal")

plt.title("Temperaturas en invierno en New York de 1900-1999")
plt.grid()
plt.legend()
plt.grid()
plt.legend()
plt.xlabel("Año")
plt.ylabel("Temperatura")

