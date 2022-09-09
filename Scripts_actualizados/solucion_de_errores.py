# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 02:36:20 2022

@author: Julián
"""
# Ejercicio 3.5
# No está contemplada la A mayúscula, agregué el 'or' en la línea 19

# El 'while' se corta si el primer caracter no es una 'a' o 'A' 
# (de ahora en más 'A' para referirme a las dos).
# Lo arreglé moviendo el 'else' fuera del loop, cortando la ejecución
# de la función con 'break' ni bien encuentre una 'A'. Si nunca se corta el
# loop, el return es False
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
            break
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
#Agrego un caso de prueba que demuestra que funciona el para el caso False
tiene_a('Nosotros no somos como los Orozco. Yo los conozco, son ocho los monos')
#%%
# Ejercicio 2.6
# Faltaban dos puntos en la definición, el while, el if
# False estaba mal escrito, el operador '==' estaba escrito como '='
# y no se contemplaba la 'A' mayúscula

#%%
# Ejercicio 2.7
# La función está pensada para strings pero 1984 es un entero
# Lo arreglé cambiando el nomre del parámetro a '_input' y definiendo
# expresion=str(_input)
#%%
# Ejercicio 2.8
# No tiene return entonces no devuelve nada. Agregué return c
#%%
# Ejercicio 2.9
# el registro es un diccionario con keys repetidas, por lo tanto al indicarle 
# registro[encabezado[0]]=fila[0] (es decir, registro['nombre']= alguna fruta) 
# luego de siete iteraciones
# ya hay seis entradas más que tienen como key la palabra 'nombre', luego las cambian
# todas sobrescribiéndolas por el nuevo valor. El último es "Naranja" y por eso
# aparece repetido tantas veces.

# Esto se arregla sobreescribiendo el registro en cada vuelta del ciclo for, o
# sea moviendo registro={} justo debajo del for fila in filas:

