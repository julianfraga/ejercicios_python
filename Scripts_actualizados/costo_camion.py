# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:17:02 2022

@author: Julián
"""

import os
import csv
archivo=r'.\camion.csv'
def costo_camion(archivo):
    costo_total=0
    with open(archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
    
        for row in rows:
            headers = next(f).split(',')
            for line in f:
                if line:
                    row = line.split(',')
                    fruta, cajones, precio_cajon= row[0], int(row[1]), float(row[2])
                    
                    costo_total=costo_total+cajones*precio_cajon
    print(f'El costo total es de ${costo_total}')
    return(costo_total)

