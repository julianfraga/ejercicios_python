#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 12:03:29 2022

@author: Julián Fraga

changelog 3/11:
    + Agrego casteo a booleano en la clase Cola
    + Modifico sintaxis obsoleta cambiando "not self.items.esta_vacia()" por 
      su equivalente "bool(self.items)"
"""

class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self, contenido_inicial=None):
        '''Crea una cola vacia.'''
        if contenido_inicial:
            self.items=contenido_inicial
        else:
            self.items = []
        

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if not self:
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    # Casteos y metodos especiales
    
    def __str__(self):
        return f'{self.items}'
    
    def __repr__(self):
        return f'Cola({self.items})'
    
    def __bool__(self):
        return len(self.items) != 0
    
    def __len__(self):
         return len(self.items)
             


class TorreDeControl:

    def __init__(self, arribos_ini=None, partidas_ini=None):
        '''Crea dos colas vacias.'''
        self.arribos = Cola(arribos_ini)
        
        self.partidas = Cola(partidas_ini)
      

    def nuevo_arribo(self, avion_aire):
        '''Agrega un avión al final de la cola arribos'''
        self.arribos.encolar(avion_aire)

        
    def nueva_partida(self, avion_tierra):
        '''Agrega un avión al final de la cola partidas'''
        
        self.partidas.encolar(avion_tierra)
       
    def ver_estado(self):
        '''No anda todavía. Quiero que printee las dos listas separadas
        por un salto de línea'''
        
        if not self.arribos and not self.partidas:
            print('No hay vuelos esperando')
        else:
            if self.arribos:
                print(f'Vuelos esperando para aterrizar: { ", ".join(self.arribos.items) }')
            else:
                print('No hay vuelos esperando para aterrizar')
            if self.partidas:
                print(f'Vuelos esperando para despegar: { ", ".join(self.partidas.items) }')
            else:
                print('No hay vuelos esperando para despegar')
    
    def asignar_pista(self):
        '''Desencola arribos. Si no hay más arribos desencola partidas'''
        if self.arribos:
            vuelo=self.arribos.desencolar()
            print(f'El vuelo {vuelo} aterrizó con éxito')
            
        elif self.partidas:
            vuelo=self.partidas.desencolar()
            print(f'El vuelo {vuelo} despegó')
            
        else:
            print('No hay aviones en esperando pista')
    
    def __str__(self):
        return(f'Arribos: {self.arribos} \nPartidas: {self.partidas}')
    
    def __repr__(self):
        return f'TorreDeControl({self.arribos}, {self.partidas})'

