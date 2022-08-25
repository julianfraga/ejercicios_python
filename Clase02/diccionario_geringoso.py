# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 19:31:23 2022

@author: Julián
"""
def diccionario_geringoso(lista):
    if lista:
        lipistapa={}
        for i in range(len(lista)):
            lipistapa[lista[i]]=geringoso(lista[i])
    return lipistapa