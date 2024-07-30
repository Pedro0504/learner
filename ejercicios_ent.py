# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 08:19:43 2024

@author: pedro
"""

#Entrevista técnica
#1. definir una función max sin usar la función 
#python tiene incorporada.
def find_max(a,b):
    m = 0
    if a>b:
        m=a
    elif b>a:
        m=b
    else:
        m = a
    return m
#print(find_max(5,5))
#2.Definir una función max de 3 que tome 3 números
#y regrese el mayor.
def max_tres(a,b,c):
    m = 0
    if a>b and a>c:
        m=a
    elif b>a and b>c:
        m=b
    elif c>a and c>b:
        m=c
    else:
        m = a
    return m
print(max_tres(-5,20,6))