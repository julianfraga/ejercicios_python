#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Created on Thu Oct  6 12:54:27 2022
@author: Julián
Fileparser con corrector de tipo de datos
Aplicalo como fileparse.parse_csv(*args, **kwargs)
changelog:
    +14/10 toma un archivo iterable como argumento en vez de una ruta
"""
import csv

def parse_csv(archivo, select = None, types= None, has_headers=True, silence_errors = False):
    ''' 
    Toma un iterable (en el contexto de csv.reader()) y devuelve una lista
    de diccionarios con los encabezados como keys.
    
    Argumentos opcionales "select" y "types", siendo "select" los encabezados
    de las columnas específicas a mirar y "types" el tipo de dato correspondiente
    a la columna. Se puede especificar uno, otro, ambos o ninguno.
    
       
    '''
    filas = csv.reader(archivo)
    if has_headers:
        encabezados = next(filas)
    elif not has_headers and select:
        raise RuntimeError("Para seleccionar, necesito encabezados.")

    # Si se indicó un selector de columnas,
    # buscar los índices de las columnas especificadas.
    # Y en ese caso achicar el conjunto de encabezados para diccionarios

    if select:
        indices = [encabezados.index(nombre_columna) for nombre_columna in select]
        encabezados = select
    elif not has_headers and types:
        indices=range(len(types))
    else:
        indices = []

    registros = []
    contador=0
    for fila in filas:
        contador+=1
        # Saltear filas vacías
        if not fila:    
            continue
        # Filtrar la fila si se especificaron columnas
        if select:
            fila = [fila[index] for index in indices] 
            
        # Armar el diccionario si especifiquñé headers, 
        # si no es simplemente una lista
        if has_headers:
            registro = dict(zip(encabezados, fila))
        else:
            registro=list(fila)
            
        # Corregimos tipo de datos si types está especificado
        if types:
            if not indices:
                indices=range(len(encabezados))
            if has_headers:
                try:
                    for indice, valor in enumerate(encabezados):
                        registro[valor]=types[indice](registro[valor])
                    registros.append(registro)
                except ValueError as e:
                    if silence_errors:
                        continue
                    else:
                        print(f'Advertencia en fila {contador}:', e)
                        print(f'Esta fila causó el error: {fila}')
            else:
                for i in indices:
                    registro[i]=types[i](registro[i])
                registros.append(tuple(registro))
        else:
            registros.append(registro)
    return registros
