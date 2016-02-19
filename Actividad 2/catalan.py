# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 15:22:17 2016

@author: Reyna
"""


   
  n, C1, C2 = 0,1,1
while(C2 < 1000000): 
    print(C2)
    C2= C1*(4*n+2)/(n+2)
    n=n+1
    C1=C2
    