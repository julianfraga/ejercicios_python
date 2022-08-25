# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 13:44:36 2022

@author: Julián
"""

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