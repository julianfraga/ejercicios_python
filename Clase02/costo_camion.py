# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:17:02 2022

@author: Julián
"""

import os
import csv
os.chdir(r'D:\Documentos\UNSAM\Programacion\ejercicios_python\Data')
path=os.getcwd()
costo_total=0
with open(path+r'\camion.csv', 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)

    for row in rows:
        print(row)
        
        
        headers = next(f).split(',')
        for line in f:
            if line:
                row = line.split(',')
                fruta, cajones, precio_cajon= row[0], int(row[1]), float(row[2])
                # print(row) 
                costo_total=costo_total+cajones*precio_cajon
print(f'El costo total es de ${costo_total}')



