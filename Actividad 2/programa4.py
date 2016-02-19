# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 20:34:57 2016

@author: Reyna
"""

n = int(input("Enter an integer: " ))

if n%2==0:
    
    print("even")
    
else:
    
    print("odd")

print ("Enter two integers, on even, one odd.")

m = int(input("Enter the first integer: 1") )

n = int(input("Enter the second integer: "))
    
while (m+n)%2==0:
    
    print ("One must be even the other odd.")
    
    m = int(input("Enter the first integer: " ))
    n = int(input("Enter the second integer: "))
    
print("The numbers you chose are",m,"and",n)
 
