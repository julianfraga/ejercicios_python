#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:14:20 2022

@author: Julián Fraga

Una serie de funciones para manejar archivos png dispersos en distintos direc-
torios y agruparlos juntos dentro de uno nuevo llamado 'imgs_procesadas'


"""

import os
from datetime import datetime as dt

def recorrer_arbol(rutini):
    '''
    Recorre un directorio y devuelve una lista de tuplas con las carpetas y ar-
    chivos encontrados. El formato es el siguiente:
    elementos = [(dir_actual), (subdir_2, ... ,subdir_n), (arch_1, ..., arch_n)]
    '''
    elementos=[]
    
    if not type(rutini)==str:
        
        raise TypeError('El argumento debe ser una cadena')
        
    for directorio in os.walk(rutini):
        elementos.append(directorio)
    return(elementos)


def archivos_png(rutini):
    '''
    Devuelve dos listas: uno con los nombres de los archivos .png encontrados
    y otra con las rutas completas
    '''
    elementos=recorrer_arbol(rutini)
    imagenes=[]
    rutas=[]
        
    for elemento in elementos:
        padre = elemento[0]
        lista_de_archivos = elemento[2]
        
        for archivo in lista_de_archivos:
            if archivo.endswith('.png'):
                ruta = os.path.join(padre, archivo)
                imagenes.append(archivo)
                rutas.append(ruta)
    return (imagenes, rutas)            


def procesar_nombre(fname):
    '''
    Procesa el nombre de la imagen asumiendo el siguiente formato:
    -> "nombreImagen_AAAAmmdd"
    
    Devuelve "nombreImagen" y el sufijo del nombre convertido a tipo "datetime"
    '''
    fecha = fname[-12:-4] 
    nombre = fname[:-13]
    date = dt.strptime(fecha, '%Y%m%d')

    return (nombre, date)


def procesar(imagen,fname):
    '''
    Procesa una imagen dada y la mueve a la carpeta imgs_procesadas
    Si no existe la carpeta en el directorio actual, la crea
    '''
    if not 'imgs_procesadas' in os.listdir():
        os.mkdir('./imgs_procesadas')
    
    nombre, fecha = procesar_nombre(fname)

    ts_modifi = fecha.timestamp()
    ts_acceso= ts_modifi
    
    ruta_nueva = os.path.join('./imgs_procesadas', imagen)
    ruta_vieja=fname

    os.rename(ruta_vieja, ruta_nueva)
    os.utime(ruta_nueva, (ts_acceso, ts_modifi))
    os.rename(ruta_nueva, ruta_nueva[:-13]+'.png')


def procesar_carpeta(directorio):
    '''
    Itera la función "procesar_imagenes()" sobre todas las subcarpetas de un
    directorio, incluído sí mismo.
    '''
    imagenes, rutas = archivos_png(directorio)
    for indice, imagen in enumerate(imagenes):
        ruta = rutas[indice]
        procesar(imagen,ruta)



def borrar_carpetas_vacias(directorio):
    '''
    Autodescriptivo sobre un directorio y sus subcarpetas
    '''
    hubo_cambios=True
    while hubo_cambios:
        arbol=recorrer_arbol(directorio)
        hubo_cambios=False
        
        for rama in arbol:
            
            if len(rama[1])==0 and len(rama[2])==0:
                os.rmdir(rama[0])
                hubo_cambios=True


if __name__ == '__main__':
    import sys
    archivos_png(sys.argv)
    
