# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 20:32:43 2016

@author: Reyna
"""

from math import sin,cos,pi

r = float(input("Introduce r: " ))

d = float(input("Introduce theta en grados: "))

d2 = float(input("Introduce phi en grados: " ))

theta = d*pi/180 
phi= d*pi/180 

x = r*sin(theta)*cos(phi)

y = r*sin(theta)*cos(phi)

z = r*cos(theta)

print ("x =",x,"y =",y, "z =",z)


