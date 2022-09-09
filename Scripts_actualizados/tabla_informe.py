#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:01:59 2022

@author: datascience
"""


# Agregué el parámetro opcional 'costo' por si queremos que el output
# nos dé también el costo del contenido. Por default no lo da
def leer_camion(nombre_archivo, costo=False):
    import csv
    camion=[]
    costo_total=0
    
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezado = next(f).split(',')
        for n_fila, fila in enumerate(filas, start=1):
            # este diccionario te zippea el encabezado definido antes del loop
            # con la fila que haya seleccionado esta iteración
            record = dict(zip(encabezado, fila))
            camion.append(record)
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio\n'])
                costo_total += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    if costo==True:
        return(camion, costo_total)
    else:
        return camion

def leer_precios(nombre_archivo):
    import csv
    dic_precios={}
    with open(nombre_archivo, 'r') as file: 
        rows = csv.reader(file)
        for row in rows:
            try:
                fruta=row[0]
                precio=float(row[1])
                dic_precios[fruta]=precio
            except:
                return(dic_precios)

def hacer_informe(precios, camion):
    informe= []
    for index, dic_camion in enumerate(camion):
        fruta=dic_camion['nombre']
        # n_cajones= dic_camion['cajones'] #no recuerdo para qué quería esta variable
        precio_venta= precios[fruta]
        precio_productor=float(dic_camion['precio\n'])
        cambio= precio_venta-precio_productor
        # el informe es prácticamente el diccionario camión con el agregadodel cambio
        dicc_interino=dic_camion
        dicc_interino['cambio']=cambio
        informe.append(dicc_interino) 
    return informe

# llamo las funciones paraluego imprimir la tabla formateada
path_camion='../Data/camion.csv'
path_precios='../Data/precios.csv'
precios=leer_precios(path_precios)
camion=leer_camion(path_camion)
informe=hacer_informe(precios, camion)


for campo in list(informe[0].keys()):
    print(f'{campo.strip().capitalize():>10s}',end=' ')
print('\n'+('-'*10+' ')*4)
for n, fila in enumerate(informe):
    nombre, cajones, precio, cambio=fila.values()
    cajones=int(cajones)
    precio=float(precio)
    print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')

