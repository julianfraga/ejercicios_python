# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 15:48:03 2022

@author: Julián
"""
import random
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]
random.sample(naipes,k=3)
