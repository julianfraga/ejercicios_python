# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 20:02:42 2022

@author: Julián
Este ejercicio está relacionado con un error muy común en Python. Escribí una 
definición de una clase Canguro que tenga:

Un método __init__ que recibe un nombre para el canguro y una lista 
(parámetro opcional) e inicializa un atributo llamado contenido_marsupio con la
lista que le pases como parámetro o como lista vacía si no le pasás nada.
 
Un método llamado meter_en_marsupio que, dado un objeto cualquiera, lo agregue 
a la lista contenido_marsupio.

Un método __str__ que devuelve una representación como cadena del objeto Canguro
indicando su nombre y los contenidos de su marsupio.
"""
class Canguro:
    
    
    def __init__(self, nombre, contenido=None):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        
        if contenido:
            self.contenido_marsupio = contenido
        else: 
            self.contenido_marsupio = []

    
    def meter_en_marsupio(self, objeto):
        """Agrega un nuevo objeto al marsupio.
        """
        self.contenido_marsupio.append(objeto)
    
    def __str__(self):
        if not self.contenido_marsupio:
            return f'{self.nombre} no tiene nada en su marsupio'
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            if type(obj)==Canguro:
                s= '    '+f'al canguro {obj.nombre}'
            t.append(s)
        return '\n'.join(t)

    
    def __repr__(self):
        return(f'Canguro({self.nombre}, {self.contenido_marsupio})')


class Canguro_malo:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        
        # Esto arregló el bug pero no entiendo por qué
        if contenido:
            self.contenido_marsupio = contenido
        else: 
            self.contenido_marsupio = []
                
    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)


    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            if type(obj)==Canguro_malo:
                s= '    '+f'al canguro malo {obj.nombre}'
            t.append(s)
        return '\n'.join(t)
    
    def __repr__(self):
        return(f'Canguro_malo({self.nombre}, {self.contenido_marsupio})')
#%%
madre=Canguro('mama', ['El salame más largo del mundo después de Nik'])
cangurin=Canguro('cangurin')

madre.meter_en_marsupio(cangurin)
madre.meter_en_marsupio('dos PBI')

cangurin.meter_en_marsupio('a Marcelo Polino')
print(madre)
print(cangurin)


madre_abandonica=Canguro_malo('Artura la cangura', ['unos puchos', 'llaves del auto', 'la coartada "voy a comprar puchos y vuelvo"'])
hijo_delincuente=Canguro_malo('Pascual el marsupial', ['gomera', 'la motito de carlitos'])
madre_abandonica.meter_en_marsupio(hijo_delincuente)
print(madre_abandonica)
print(hijo_delincuente)

