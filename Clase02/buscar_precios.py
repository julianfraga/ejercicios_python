# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 15:15:03 2022

@author: Julián
"""

def buscar_precios(fruta_input, verbose=True):
    import os
    os.chdir(r'D:\Documentos\UNSAM\Programacion\ejercicios_python\Data')
    path=os.getcwd()
    f = open(path+r'\precios.csv', 'rt')
    fruta=str(fruta_input)
    token=False
    precio= 'null'
    
    # try:
    for line in f:
        row = line.split(',')
        if fruta[0].upper()+fruta[1:].lower()==row[0]:
            precio=float(row[1])
            token=True
    if token:
        print(f'El precio del cajón de {fruta} es de ${precio}')
    else:
    
        print(f'{fruta} no es un elemento de la lista')
    
    # if fruta[0].upper()+fruta[1:].lower() not in line: 
        #podría hacer algo como esto para ahorrarme la variable token?
    
    # except :
    #     print('Debe ingresar una palabra en el campo de búsqueda')    
    
    # Dejo esto como placeholder para manejar posibles errores
            
    f.close()

    return precio
