# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 01:55:08 2022

@author: Julián
"""

import csv
import sys

def leer_camion(archivo_camion):
    camion=[]

    with open(archivo_camion, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in (rows):
            s={}
            s['nombre']= row[0]
            s['cajones']= int(row[1])
            s['precio']=float(row[2])
            camion.append(s)

    return camion

def leer_precios(archivo_precios):
    dic_precios={}
    with open(archivo_precios, 'r') as file: 
        rows = csv.reader(file)
        for row in rows:
            try:
                fruta=row[0]
                precio=float(row[1])
                dic_precios[fruta]=precio
            except:
                a=1 # no sé cómo dejar el bloque except vacío
                    # esta línea es casi un placehloder 
    return(dic_precios)

def ganancia(archivo_camion, archivo_precios):
    ganancia=0
    venta=0
    costo=0
    camion=leer_camion(archivo_camion)
    precios=leer_precios(archivo_precios)
    # en el siguiente loop uso enumerate
    # para desdoblar el iterador en un índice (i, j)
    # y el elemento sobre el cual realmente busco iterar
    # que son los diccionarios de la lista 'camión'
    # y los nombres de las frutas en el diccionario 'precios'
    # Los índices los descarto.
    for i, diccionario in enumerate(camion):
        # print(i, diccionario)
        for j, fruta in enumerate(precios):
             # print(indice, fruta)
            if diccionario['nombre']==fruta:
                # print (fruta, 'el precio de venta' ,precios[fruta], 'y el costo es', diccionario['precio'])
                cajones=int(diccionario['cajones'])
                precio_lista=float(diccionario['precio'])
                precio_venta=float(precios[fruta])
                
                # ganancia_parcial=cajones*(precio_venta-precio_lista)
                venta+=precio_venta*cajones
                costo+=precio_lista*cajones
    ganancia= venta-costo
    print(f'El costo de la mercancía fue de ${costo:.2f}')
    print(f'Se recaudaron ${venta:.2f} con la venta de los productos')
    print(f'Esto significa una ganancia de ${ganancia:.2f}')
    return(ganancia)

# Agregué el siguiente try-except porque quería correrlo a veces desde el
# directorio '.../ejercicios_python' 
# otras desde '.../ejercicios_python/Clase03'
# y otras pasándole los archivos yo como argumentos
# Con esto me aseguro de que sí o sí tiene un default para agarrar
# sin importar desde dónde lo esté corriendo
# Tal vez es medio rebuscado pensar en que podría querer correrlo desde
# el primer directorio. No sé
if len(sys.argv) == 3:
    archivo_camion = sys.argv[1]
    archivo_precios = sys.argv[2]
    ganancia(archivo_camion, archivo_precios)
else:
    try:
        archivo_camion = '../Data/camion.csv'
        archivo_precios='../Data/precios.csv'
        ganancia(archivo_camion, archivo_precios)
    except:
        archivo_camion = './Data/camion.csv'
        archivo_precios='./Data/precios.csv'
        ganancia(archivo_camion, archivo_precios)
    
