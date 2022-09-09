# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 20:50:18 2022

@author: Julián
    Comentarios para el/la/le docente: me costó horrores debuggear este script
fue el más difícil hasta la fecha. El problema principal fue encontrar una manera
relativamente compacta de salir del ciclo while, que a su vez estaba tratando
de usar como manera compacta de escanear la lista de números hasta agotarse las
acciones por hacer. No sé si había una forma más elegante y me la compliqué
o era así de trabajoso.

    Me tomé el trabajo de comentar todo mi proceso de razonamiento porque
tal vez a futuro encuentro listas que rompen mi programa, casos no considerados
    Quisiera saber si tanto comentario aporta o más bien molesta.
    Saludos quien lea.
"""

#similar a la función tiene_a, sólo informa si la lista tiene algún cero
def tiene_cero(lista):
    n = len(lista)
    i = 0
    token=False
    while i<n:
        if lista[i] == 0:
            token= True
            break
        i += 1
    return token
# recorre todos los elementos de la lista y cuando encuentra un cero anota el
# índice
def buscar_ceros(lista):
    indices=[]
    for i, elemento in enumerate(lista):
        if elemento==0:
            indices.append(i)
    return indices

    
def propagacion(caja):
    # creo una copia privada de la lista ingresada
    # para no modificar el input
    caja_propagada=list(caja)
    # si es una lista sin ceros, el return es idéntico al input original
    # me ahorro de evaluar todas estas condiciones (creo, tal vez no ahorra nada)
    if not tiene_cero(caja):
        print('nada más que hacer')
    # en caso de tener algún cero, entro en el siguiente bloque
    else:
        # banderita asumiendo de entrada que haré algún cambio en la lista
        # en la vuelta del ciclo que estoy por ejecutar
        vuelta_cambios=True

        while vuelta_cambios==True:
            indices=buscar_ceros(caja_propagada)
            # de entrada asumo que no tengo que cambiar el estado del cero
            # en el cuál estoy parado
            cambiar_estado=False
            # para todos los lugares en los que haya un cero:
            for i in indices:
                #para cada iteracion del for asumo de vuelta que no cambio nada
                cambiar_estado=False
                
                # si el índice no es el primero ni el último
                if i<len(caja)-1 and i!=0:
                    if caja_propagada[i-1]==1 or caja_propagada[i+1]==1:
                        cambiar_estado=True
                # si no, si el índice es el último y 
                # el anterior resulta ser un 1
                elif i==len(caja)-1 and caja[i-1]==1:
                    cambiar_estado=True
                
                # si no, si el índice es el primero y el siguiente
                # resulta ser un 1
                elif i==0 and caja_propagada[i+1]==1:
                    cambiar_estado=True
                
                # y si no es ninguna de las anteriores, no realicé ningun cambio
                else:
                    cambiar_estado=False
                
                # si realicé un cambio
                if cambiar_estado:
                    # anoto que en esta vuelta algún cambio hice
                    vuelta_cambios=True
                    # el cero en el que estoy parado pasa a ser un 1
                    caja_propagada[i]=1
                # vuelvo a iterar para el siguiente índice
            
            # si en la vuelta que acaba de pasar no hice un cambio en ningún
            # momento entonces salgo del while. Si hice algún cambio me quedo
            if cambiar_estado==False:
                vuelta_cambios=False
        print('La piromanía (del griego πυρός pyrós, "fuego" y μανία manía "locura")')
        print('según el DSM-V, es un trastorno del control de impulsos relacionado ')
        print('con la provocación de incendios y la atracción por el fuego')
    return caja_propagada

propagacion([1, 0,0,0,1,0,-1,0,-1, 1])
