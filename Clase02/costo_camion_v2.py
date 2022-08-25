# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:17:02 2022

@author: Julián
"""

import os
import csv
path=r'D:\Documentos\UNSAM\Programacion\ejercicios_python\Data'
os.chdir(path)
costo_total=0
with open(path+r'\camion.csv', 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        fruta, cajones, precio_cajon= row[0], int(row[1]), float(row[2])
        costo_total=costo_total+cajones*precio_cajon

print(f'El costo total es de ${costo_total}')



