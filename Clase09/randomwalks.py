# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:56:22 2022

@author: Julián
"""

# Ejercicio 9.1
import matplotlib.pyplot as plt

fig = plt.figure()
plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja la curva
plt.xticks([]), plt.yticks([]) # saca las marcas

plt.subplot(2, 3, 4) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot([0,1],[0.5,0.5])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 6) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])

plt.show()

#%%
# Ejercicio 9.2 - items 1, 2

import numpy as np


def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()


N = 100000
plots = 12

for plot in range(plots):
    plt.plot(randomwalk(N), label=f'plot nro {plot+1}')

plt.xlabel('Tiempo [pasos]')
plt.ylabel('Distancia al origen')
plt.title(f'{plots} Caminatas al azar de {N:0.01e} pasos')
plt.legend()
plt.show()

#%%
# Ejercicio 9.2  - ítem 3

data=[]
maximo=0
minimo=N

for plot in range(plots):
    caminata = randomwalk(N)
    alejamiento = max(np.abs(caminata))
    data.append(caminata)
    
    if alejamiento > maximo:
           maximo = alejamiento
           plot_maximo = plot
    
    if alejamiento < minimo:
        minimo = alejamiento
        plot_minimo = plot


fig = plt.figure()

plt.subplot(2, 1, 1)
for plot in range(plots): 
    plt.plot(data[plot], label=f'plot nro {plot+1}') #las 12 trayectorias
plt.title(f'{plots} Caminatas al azar de {N:0.01e} pasos')
plt.xticks([])
plt.ylim(-1000, 1000), plt.yticks([-500,0,500])


plt.subplot(2,2,3)
plt.plot(data[plot_maximo])
plt.title('La caminata que más se aleja')
plt.xticks([])
plt.ylim(-1000, 1000), plt.yticks([-500,0,500])


plt.subplot(2,2,4)
plt.plot(data[plot_minimo])
plt.title('La caminata que menos se aleja')
plt.xticks([])
plt.ylim(-1000, 1000), plt.yticks([-500,0,500])


plt.show()
