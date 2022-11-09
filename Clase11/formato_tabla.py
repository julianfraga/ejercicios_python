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
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()


class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()

class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))

class FormatoTablaHTML(FormatoTabla):
    '''
    Genera una tabla en formato HTML
    '''
    def encabezado(self, headers):
        header_html = '<th>'+'</th><th>'.join(headers)+'</th>'
        print('<tr>'+header_html+'</tr>')
    
    def fila(self, data_fila):
        fila_html='<td>'+'</td><td>'.join(data_fila)+'</td>'
        print('<tr>'+fila_html+'</tr>')  


def crear_formateador(fmt):
    if fmt == 'txt':
        formateador = FormatoTablaTXT()
    elif fmt == 'csv':
        formateador = FormatoTablaCSV()
    elif fmt == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    return formateador