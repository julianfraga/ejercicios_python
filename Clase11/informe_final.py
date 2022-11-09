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

9/11:
    +Agrego formateadores
    +Tengo problemas con ejecutando el archivo como función principal desde
    cmd porque algo mal tengo en el environment local. Por esto mismo no pude
    debugear así que no estoy seguro de si corre bien por linea de comandos
"""
import fileparse as fp
import gzip
import formato_tabla

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


def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe a partir de un archivo de camión
    y otro de precios de venta.
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = dict(leer_precios(archivo_precios))

    # Crear los datos para el informe
    data_informe = hacer_informe(camion, precios)
    
    # Elige formato
    formateador = formato_tabla.crear_formateador(fmt)
    
    # Imprime el informe
    imprimir_informe(data_informe, formateador)



def funcion_principal(argumentos, fmt):
    try:
        nombreArchivoCamion=argumentos[1]
        nombreArchivoPrecios=argumentos[2]
        imprimir_informe(nombreArchivoCamion, nombreArchivoPrecios, fmt)
    except Exception as e:
        print('No se pudo ejecutar por el siguiente motivo:',e)


if __name__ == '__main__':
    import sys
    funcion_principal(sys.argv, fmt='txt')
