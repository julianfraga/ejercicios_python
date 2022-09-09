# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 21:58:17 2022

@author: Julián
"""
numeros=range(0,10)
tabla={}
for i in numeros:
    item=0
    lista=[0]
    for j in numeros[:-1]: # consulta por qué tengo que poner este [:-1]??
        item+=i            # si no lo pongo me devuelve una tabla de 9x10
        lista.append(item) # pero por qué pasa eso?
    tabla[i]=lista

string=' '*6
for n in tabla.keys(): #armo la fila de encabezados iterando porlas keys de la tabla
    string+=f'{n:>4d}'
print(string)
print(('-'*4)*10+('-')*6)
for key in list(tabla.keys()):
    linea=''
    for i in list(tabla.keys()):
        linea+=f'{tabla[key][i]:>4d}'
        # linea+=' '*5+str(tabla[key][i]).strip('[]')
        linea.strip(',')
    print(f'{key:<2d}:'+3*' '+f'{linea}')


