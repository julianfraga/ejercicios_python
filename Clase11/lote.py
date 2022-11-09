# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 18:27:36 2022

@author: Julián
"""
class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        return self.cajones * self.precio

    def vender(self, ncajones):
        self.cajones -= ncajones
    
    def __repr__(self):
        return f'Lote("{self.nombre}", {self.cajones}, {self.precio})'

class MiLote(Lote):
    def rematar(self):
        self.vender(self.cajones)
        
# armo una lista de lotes. Por qué es práctico esto? no le veo la utilidad
import informe_final
camion = informe_final.leer_camion('../Data/camion.csv')
lista_de_lotes=[]
for lote in camion:
    lotecin=Lote(*lote.values())
    lista_de_lotes.append(lotecin)
