# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 20:29:55 2016

@author: Reyna
"""
from math import sin,cos,pi

r = float(input("introduce r: " ))

d = float(input("Ingresa theta en grados: "))

theta = d*pi/180

x = r*cos(theta)

y = r*sin(theta)

print("x=",x,"y=",y)
