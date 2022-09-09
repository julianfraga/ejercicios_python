# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 15:49:40 2022

@author: Julián
"""
from math import pi
print("Ejercicio 3: Sea una vaca esférica de radio [___] sin rozamiento")
print("(Ingrese un número positivo)")
radio = input()
token=False
while token==False:
    try:
        radio=float(radio)
        
        if type(radio)==float or type(radio)==int:
            token=True
            if float(radio)<=0:
                token=False
                print("p o s i t i v o  le dije")
                print("O se lo explico con dibujitos?")
                radio = input()
                
    except:
       token=False
       print("En numeritos, caballerx")
       radio = input()

if token==True:
    vol=round(4/3*math.pi*radio**3, 2)
    print(f"El volumen de una vaca de radio {radio}m es {vol}m^3")
