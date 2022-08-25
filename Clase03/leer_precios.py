# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 13:45:41 2022

@author: Julián
"""

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
                a=1 #no sé cómo dejar el bloque except vacío                
    return(dic_precios)