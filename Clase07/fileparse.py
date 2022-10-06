# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 12:54:27 2022

@author: Julián

Fileparser con corrector de tipo de datos

Aplicalo como fileparse.parse_csv(*args, **kwargs)
"""
import csv


def parse_csv(nombre_archivo, select = None, types= None, has_headers=True):
    ''' 
    Toma un archivo CSV y devuelve una lista de diccionarios con los 
    encabezados como keys.
    
    Argumentos opcionales "select" y "types" siendo "select" los encabezados
    de las columnas específicas a mirar y "types" el tipo de dato correspondiente
    a la columna. Se puede especificar uno, otro, ambos o ninguno.
    
       
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        if has_headers:
            encabezados = next(filas)
    
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
        for fila in filas:
            # Saltear filas vacías
            if not fila:    
                continue
            # Filtrar la fila si se especificaron columnas
            if select:
                fila = [fila[index] for index in indices]     
            #Armar el diccionario si especifiquñé headers
            if has_headers:
                registro = dict(zip(encabezados, fila))
            else:
                registro=list(fila)
            # Corregimos tipo de datos si types está especificado
            if types:
                # si no se especificaron columnas, "indices" es un range
                # del largo del vector de encabezados
                if not indices:
                    indices=range(len(encabezados))
                if has_headers:
                    for i in indices:
                        registro[encabezados[i]]=types[i](registro[encabezados[i]])
                    registros.append(registro)
                else:
                    for i in indices:
                        registro[i]=types[i](registro[i])
                    registros.append(tuple(registro))
    return registros
                        
