# -*- coding: utf-8 -*-
# formato_tabla.py
"""
Created on Tue Nov  8 18:42:12 2022

@author: Julián

Hice que la clase haga algo efectivamente porque si no no me salía.

Es un comienzo. Por alguna razón cuando llamo FormatoTabla.encabezado(headers)
tengo que ponerle algún valor como primer argumento para que ande. Consultar

"""

class FormatoTabla:
    def __init__(self):
        self.headers=None
        self.rowdata=None
        
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        encabezado=''
        for columna in headers:
            encabezado+=f'{columna:>12}'
        print(encabezado)
        print('   ---------'*len(headers))
        # raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        fila_actual=''
        for data in rowdata:
            fila_actual+=f'{data:>12}'
        print(fila_actual)
        
        raise NotImplementedError()
#%%
from informe_final import leer_camion, leer_precios, hacer_informe

def imprimir_informe2(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    camion = leer_camion(data_informe[0])
    precios = leer_precios(data_informe[1])
    informe = hacer_informe(camion, precios)
    
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)
        
data_informe=['../Data/camion.csv', '../Data/precios.csv']
imprimir_informe2(data_informe, FormatoTabla)


header=['Nombre', 'Cantidad', 'Precio', 'Cambio']
FormatoTabla.encabezado(2, header)
#%%

# formateador=FormatoTabla()
# formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
# headers=['Nombre', 'Cantidad', 'Precio', 'Cambio']
