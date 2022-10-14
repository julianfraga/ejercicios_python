# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 14:24:53 2022

@author: Julián

Este módulo contiene todas las funciones de lectura y confección de informes
del conjunto de archivos de precios de frutas.


Changelog 

13/10:
    +leer_precios devolvía una lsita de diccionarios -> ahora devuelve un diccionario
    +Agregué if __name__=='__main__' para ejecutarlo como func. ppal.
    +Corre en commandline
14/10:
    +leer_camion y leer_precios son compatibles con la última versión de
     fileparse.parse_csv()
"""
import fileparse as fp
import gzip


def leer_camion(nombre_archivo, extension='csv'):
    
    if extension=='gz':
        archivo=gzip.open(nombre_archivo, 'rt')
    else:
        try:
            archivo=open(nombre_archivo, 'rt')
        except Exception as e:
            print('leer_camion no soporta la extensión {extension}')
            print(e)
            raise
        
    camion = fp.parse_csv(archivo, types=[str, int, float])
    archivo.close()
    return camion


def leer_precios(nombre_archivo, extension='csv'):
    
    if extension=='gz':
        archivo=gzip.open(nombre_archivo, 'rt')
    else:
        try:
            archivo=open(nombre_archivo, 'rt')
        except Exception as e:
            print('leer_camion no soporta la extensión {extension}')
            print(e)
            raise
            
    listaDeTuplas=fp.parse_csv(archivo, types=[str,float], has_headers=False)
    precios= {listaDeTuplas[i][0]:listaDeTuplas[i][1] for i in range(len(listaDeTuplas))} 
    archivo.close()
    return precios


def hacer_informe(camion, precios):
    lista = []
    
    for lote in camion:
        precio_venta = precios[lote['nombre']]
        cambio = precio_venta - lote['precio'] 
        t = (lote['nombre'], lote['cajones'], lote['precio'], cambio)
        lista.append(t)
    
    return lista


def imprimir_informe(nombre_archivo1, nombre_archivo2):
    ''' imprime el informe '''
    camion = leer_camion(nombre_archivo1)
    precios = leer_precios(nombre_archivo2)
    informe = hacer_informe(camion, precios)

    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
    
    return
    

def informe_camion(nombreArchivoCamion, nombreArchivoPrecios):
    imprimir_informe(nombreArchivoCamion, nombreArchivoPrecios)


def funcion_principal(argumentos):
    try:
        nombreArchivoCamion=argumentos[1]
        nombreArchivoPrecios=argumentos[2]
        imprimir_informe(nombreArchivoCamion, nombreArchivoPrecios)
    except Exception as e:
        print('No se pudo ejecutar por el siguiente motivo:',e)


if __name__ == '__main__':
    import sys
    funcion_principal(sys.argv)
