# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:22:51 2022

@author: Julián
"""
def valor_absoluto(n):
    '''
    Devuelve el valor absoluto de 'n'
    
    Pre: el argumento es de tipo int o float
    Pos: la función devuelve su valor absoluto como el mismo tipo de dato
    '''
    if n >= 0:
        return n
    else:
        return -n
    
def suma_pares(l):
    '''
    Suma los elementos pares de una lista
    
    Pre: l es una lista de números enteros
    Pos: la función devuelve el resultado de la suma de los enteros de la lista
    '''
    
    res = 0 
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

def veces(a, b):
    '''
    Suma 'a' una cantidad 'b' de veces
    
    Pre: 'a' es un número entero o de punto flotante y 'b' un número natural
    Pos: Devuelve el resultado de hacer a*b dadas las precondiciones
    '''
    res = 0
    nb = b
    while nb != 0:
        # print(nb * a + res)
        res += a
        nb -= 1
    return res

def collatz(n):
    '''
    Devuelve la cantidad de elementos de la sucesión de Collatz 
    que empieza en 'n' y termina en C_i=1
    
    Pre: 'n' es  un número natural (int !=0)
    Pos: Devuelve la cantidad de iteraciones realizadas antes de llegar al 1
    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
