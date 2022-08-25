# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 18:41:02 2022

@author: Seba, practica 3
""" 
#lista como contenedores 
camion = [
    ('pera', 100, 490),
    ('naranja', 50, 91),
    ('limon', 150, 83)
    ]
#%% #Armar una lista de cero
registros = []

registros.append(('Pera', 100, 490 ))
registros.append(('Naranja', 50, 91))
#%% #Armar una lista desde un archivo
registros = []
with open ('../Data/camion.csv', 'rt') as f:
    header = next(f)
    for line in f:
        row = line.split(',')
        registros.append((row[0], int(row[1]), float(row[2])))
        #%% 
with open ('../Data/camion.csv', 'rt') as f:
    data= f.read()
    print(data)
#%% #Armar un diccionario
precios = {
   'Pera': 513.25,
   'Limon': 87.22,
   'Naranja': 93.37,
   'Mandarina': 44.12
}
precios['Mandarina']
precios['Limon']
#%% #Armar un diccionario de cero
precios = {}
precios['Pera']= 513.25
precios['Limon']= 87.22
precios['Naranja'] = 93.37
#%% #armar diccionario a partir de un archivo
precios = {}

with open('../Data/precios.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        precios[row[0]] = float(row[1])
                
#%% #claves compuestas
feriados ={(1,1): 'Año nuevo',
           (1,5): 'dia del trabajador',
           (13,9): 'Dia del programador'
    }
#%% #conjuntos
citricos= set(['Naranja', 'Limon', 'Mandarina'])
 #los conjuntos sirven para evaluar pertenencias
citricos
'Naranja' in citricos #True

'Manzana' in citricos #False
#%% Los conjuntos tambien son utiles para eliminar duplicados
nombres = ['Naranja', 'Banana', 'Naranja', 'Pera', 'Manzana', 'Pera']
unicos=set(nombres)  # unicos = {'Manzana', 'Banana', 'Naranja', 'Pera'}
#%%
#operaciones con conjuntos
citricos.add('Banana') #agrega un elemento
citricos.remove('Limon') #elimina un elelemento

A = 45
B = 390
A | B                 # Unión de conjuntos A y B
A & B                 # Intersección de conjuntos
A - B                 # Diferencia de conjuntos


#%%
precios = {}
precios['Naranja'] = 92.45
precios['Mandarina'] = 45.12
precios

precios['Naranja']
92.45
precios['Manzana']

'Manzana' in precios
#%% #Ejercicios de correcion (debug) 
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1
#%%        
def tiene_a(expresion)
    n = len(expresion)
    i = 0
    while i<n
        if expresion[i] = 'a'
            return True
        i += 1
    return Falso
#%%
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene
#%% 3.8 #
#no hay que llamar a la funcion dos veces 
def suma(a,b):
    c = a + b

a = 2
b = 3
c = (a+b)
print(f"La suma da {a} + {b} = {c}")

#%%
#hace falta poner el diccionario adentro del for para que lo imprima bien
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)