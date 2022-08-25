# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 19:30:27 2022

@author: Julián
"""
h_ini= 100 #metros
elasticidad=3/5
rebotes=10
alturas=[]
i=0
print('Primer método: while y potencias del índice')
while i <10:
	altura_actual=h_ini*elasticidad**i
	alturas.append(round(altura_actual, 4))
	i=i+1

print (alturas)
print(' otro método usando un if')

alturas_2=[]
k=0

print('Segundo método: while>>if/else , usando el índice anterior para generar el siguiete')
while k <10:
	if len(alturas_2)==0:
		alturas_2.append(h_ini*elasticidad)
	else:
		altura_2=alturas_2[k-1]*elasticidad
		alturas_2.append(round(altura_2,4)) 
	k=k+1
print(alturas_2)
