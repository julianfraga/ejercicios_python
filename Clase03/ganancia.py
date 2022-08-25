# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 14:02:04 2022

@author: Julián
"""
def ganancia(archivo_camion, archivo_precios):
    ganancia=0
    camion=leer_camion(archivo_camion)
    precios=leer_precios(archivo_precios)
    # en el siguiente loop uso enumerate
    # para desdoblar el iterador en un índice (i, j)
    # y el elemento sobre el cual realmente busco iterar
    # que son los diccionarios de la lista 'camión'
    # y los nombres de las frutas en el diccionario 'precios'
    # Los índices los descarto.
    for i, diccionario in enumerate(camion):
        # print(i, diccionario)
        for j, fruta in enumerate(precios):
             # print(indice, fruta)
            if diccionario['nombre']==fruta:
                # print (fruta, 'el precio de venta' ,precios[fruta], 'y el costo es', diccionario['precio'])
                cajones=int(diccionario['cajones'])
                precio_lista=float(diccionario['precio'])
                precio_venta=float(precios[fruta])
                ganancia_parcial=cajones*(precio_venta-precio_lista)
                ganancia+= ganancia_parcial
    return(ganancia)