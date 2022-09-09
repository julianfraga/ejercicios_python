# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 23:56:47 2022

@author: Julián
"""
def geringoso(cadena):
    capadepenapa = ''
    vocales='aeiou'
    if cadena:
        for c in cadena:
            if c in vocales:
                capadepenapa=capadepenapa+c+'p'+c
            else:
                capadepenapa=capadepenapa+c
        print(capadepenapa)
    return capadepenapa

 


