# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 19:42:28 2022

@author: Seba D'Amelio
"""
import csv
def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in (rows):
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
    return camion
#%%
camion=leer_camion('../Data/camion.csv')
total=0.0
for nombre, cajones, precio in camion:
    total+= cajones*precio
    #Observación: la instrucción += es una abreviación.
   #Poner a += b es equivalente a poner a = a + b
print(total)
#%%
import csv
def leer_camion(nombre_archivo):
    camion=[]

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in (rows):
            s={}
            s['nombre']= row[0]
            s['cajones']= int(row[1])
            s['precio']=float(row[2])
            camion.append(s)

    return camion


camion= leer_camion('../Data/camion.csv')

#%% diccionario como contenedores
import csv
def leer_precios(nombre_archivo):
    dic_precios={}
    with open('../Data/precios.csv', 'r') as file: 
        rows = csv.reader(file)
        for row in rows:
            try:
                fruta=row[0]
                precio=float(row[1])
                dic_precios[fruta]=precio
            except:
    return(dic_precios)
path_camion='../Data/camion.csv'
path_precios='../Data/precios.csv'

precios=leer_precios('../Data/precios.csv')
camion=leer_camion(path_camion)
#%%

costo_total=costo_camion()
frutas=[]
for i, item in enumerate(camion):
    frutas.append(item['nombre'])

for fruta in lista_de_frutas:

    cajones*precio-costo
    #   row = line.split(',')
        costo_parcial= int(row[1])*float(row[2])
        costo_total= costo_total+costo_parcial
        
#%%

for i, fruta in enumerate(camion):
    if fruta in
    venta= camion[0]
    venta['cajones']*venta['precio']
    costo_parcial=venta['cajones']*venta['precio']-costo_camion
#%%
ganancia=0
for i, diccionario in enumerate(camion):
    # print(i, diccionario)
    for indice, fruta in enumerate(precios):
         # print(indice, fruta)
        if diccionario['nombre']==fruta:
            print (fruta, 'el precio de venta' ,precios[fruta], 'y el costo es', diccionario['precio'])
            cajones=int(diccionario['cajones'])
            precio_lista=float(diccionario['precio'])
            precio_venta=float(precios[fruta])
            ganancia_parcial=cajones*(precio_venta-precio_lista)
            ganancia=ganancia+ganancia_parcial
