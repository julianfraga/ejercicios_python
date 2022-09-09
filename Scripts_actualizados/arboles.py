# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 13:30:08 2022

@author: Julián
"""
# Ejercicio 4.13

def leer_parque(nombre_archivo, parque):
    import csv
    parque_lista=[]
    with open(nombre_archivo, 'rt', encoding="utf8") as f:
        filas = csv.reader(f)
        encabezado = next(f).split(',')
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezado, fila))
            # me saco el \n de encima de la última llave renombrándola
            record['coord_y'] = record.pop('coord_y\n') 
            if record['espacio_ve']==parque:
                parque_lista.append(record)
                
    # TODO
        # Encontrar la manera elegante de formatear los datos
        # en el tipo de dato necesario porque por default son todos
        # strings. Una opción es volverse loco con el siguiente try except
        # pero no es para nada elegante, fino ni distinguido
        
                # try:
                #   record['long']=float(record['long'])
                #   lat=float(record['lat'])
                #   id_arbol=int(record['id_arbol'])
                #   altura_tot=int(record['altura_tot'])
                #   diametro=int(record['diametro'])
                #   inclinacio=int(record['inclinacio'])
                #   id_especie=int(record['id_especie'])
                #   nombre_com=str(record['nombre_com'])
                #   nombre_cie=str(record['nombre_cie'])
                #   tipo_folla=str(record['tipo_folla'])
                #   espacio_ve=str(record['espacio_ve'])
                #   ubicacion=str(record['ubicacion'])
                #   nombre_fam=str(record['nombre_fam'])
                #   nombre_gen=str(record['nombre_gen'])
                #   origen=str(record['origen'])
                #   coord_x=float(record['coord_x'])
                #   coord_y=float(record['coord_y'])
    
                # Esto atrapa errores en los int() y float() de arriba.
            # except ValueError:
            #     print(f'Fila {n_fila}: No pude interpretar: {fila}')

        return parque_lista
    
archivo='../Data/arbolado.csv'
nombre_parque='GENERAL PAZ'
parque=leer_parque(archivo, nombre_parque)
if nombre_parque=='GENERAL PAZ' and len(parque)==690:
    print('Yay!')
else:
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaah!!')
#%%
# Ejercicio 4.14
def listar_especies(parque):
    set_especies=set([])
    
    for i, arbol in enumerate(parque):
        especie=arbol['nombre_com']
        if especie not in set_especies: #si aún no agregué la especie al set
            set_especies.add(especie) # la agrego
    return(set_especies)
listar_especies(parque)
#%%
# Ejercicio 4.15
def contar_ejemplares(lista_arboles):
    set_especies=listar_especies(lista_arboles) #armo un set llamando la func anterior
    contador=dict.fromkeys(set_especies, 0) #armo diccionario vacio a llenar por mi contador

    for especie in set_especies: # para una especie de la lista
        total_arboles=0
        for i, arbol in enumerate(lista_arboles):
            if arbol['nombre_com']==especie:# si este arbol pertenece a la especie
                total_arboles+=1            # añadí uno al contador
        contador[especie]=total_arboles     # genero una entrada en el diccionario tipo 
                                            # {especie: cuentas}
    return(contador)

conteo=contar_ejemplares(parque) #chequeo
if nombre_parque=='GENERAL PAZ' and conteo['Palo borracho rosado']==44:
    print('Yay!')
else:
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaah!!')
#%%
def leer_arbol(nombre_archivo):
    import csv
    arboleda=[]
    def ignorar_keys(diccionario, keys):
        return {x: diccionario[x] for x in diccionario if x not in keys}
    keys_excluir={'long', 'lat', 'espacio_ve', 'coord_x', 'coord_y'}
    with open(nombre_archivo, 'rt', encoding="utf8") as f:
        filas = csv.reader(f)
        encabezado = next(f).split(',')
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezado, fila))
            # me saco el \n de encima de la última llave renombrándola
            record['coord_y'] = record.pop('coord_y\n') 
            record=ignorar_keys(record, keys_excluir)
            arboleda.append(record)
    return arboleda
    
nombre_archivo='../Data/arbolado.csv'
arboleda=leer_arbol(nombre_archivo)
#%%
def alt_diam(arboleda, especie):
    lista=[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie]
    return lista

def medidas_de_especies(arboleda, especies):
    medidas={especie:alt_diam(arboleda, especie) for especie in especies}
    return medidas
especies=['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
nombre_archivo='../Data/arbolado.csv'
arboleda=leer_arbol(nombre_archivo)
medidas=medidas_de_especies(arboleda, especies)

if (len(medidas['Eucalipto']), len(medidas['Palo borracho rosado']), len(medidas['Jacarandá']))== (4112, 3150, 3255):
    print('Los diccionarios tienen las medidas esperadas')