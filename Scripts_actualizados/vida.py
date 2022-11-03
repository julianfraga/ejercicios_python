# -*- coding: utf-8 -*-

''' 
 La función toma tu fecha de nacimiento y te devuelve la cantidad de segundos
 que viviste (asumiendo que naciste a las 00:00hs de tu fecha de 
 nacimiento). La función toma como entrada una cadena en 
 formato 'dd/mm/AAAA' y devuelve un float
'''

from datetime import datetime as dt

def vida_en_segundos(fecha_nac):
    
    ahora = dt.now()
    fecha_dt = dt.strptime(fecha_nac, '%d/%m/%Y')
    segundos = (ahora-fecha_dt).total_seconds()
    
    return float(segundos)

