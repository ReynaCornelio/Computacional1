# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 20:06:38 2016

@author: Reyna
"""
h = float(input("Proporciona la altura de la torre: "))
t = float(input("Ingrese el tiempo: "))
s = 0.5*9.81*t**2
print("La altura de la pelota es", h-s, "metros")

