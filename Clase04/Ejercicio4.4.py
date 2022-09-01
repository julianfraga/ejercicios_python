#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 14:35:55 2022

@author: datascience
"""


def costo_camion(archivo_camion):
    import csv
    f=open(archivo_camion, 'rt')
    filas = csv.reader(f)
    encabezados = next(f).split(',')
    costo_total=0
    for n_fila, fila in enumerate(filas, start=1):
        record = dict(zip(encabezados, fila))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio\n'])
            costo_total += ncajones * precio
        # Esto atrapa errores en los int() y float() de arriba.
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')

    return costo_total
#%%
archivo_camion='../Data/fecha_camion.csv'
camion=costo_camion(archivo_camion)
print(camion)
#%% counters
camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.1),
    ('Caqui', 150, 83.44),
    ('Naranja', 100, 45.23),
    ('Pera', 75, 572.45),
    ('Lima', 50, 23.15)
]

from collections import Counter
total_cajones = Counter()
for nombre, n_cajones, precio in camion:
    total_cajones[nombre] += n_cajones
    
    
    