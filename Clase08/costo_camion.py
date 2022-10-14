# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:17:02 2022

@author: Julián


changelog 13/10:
    +Agregué func. ppal.
    +Corre por commandline e intérprete python    
"""
import informe_final as info
def costo_camion(archivo):
    costo_total=0
    lista=info.leer_camion(archivo)
    for i in range(len(lista)):
        costo_total+=lista[i]['cajones']*lista[i]['precio']
    print(f'El costo total es de ${costo_total}')
    return(costo_total)

def funcion_principal(argumentos):
    try:
        costo_camion(argumentos[1])
    except Exception as e:
        print('No se pudo ejecutar por el siguiente motivo:',e)


if __name__ == '__main__':
    import sys
    funcion_principal(sys.argv)

    