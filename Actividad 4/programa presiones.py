# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 18:26:55 2016

@author: Reyna
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

datos = np.loadtxt('presiones.txt')
x = datos[: , 0]
y = datos [: , 1]


#forma de la función
def f(x, a, b, c):
return  a * np.exp(-b * x) + c

#Ajuste exponencial
popt, pcov = curve_fit(f,x,y)


#para graficar nuestra función

time = np.linspace(x.min(), y.max(), 100)

plt.plot(time, fitfunc(p1, time), "g-", label="Ajuste exponencial")

plt.title("Presión atmosférica vs. altitud")
plt.grid()
plt.legend()
plt.xlabel("Altitud")
plt.ylabel("presión")