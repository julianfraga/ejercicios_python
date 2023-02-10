# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 16:52:25 2022

@author: Julián
Contexto: 
Se tienen dos datasets del arbolado de la ciudad de Buenos Aires

Consigna: 
Para cada dataset armate otro seleccionando solamente las filas correspondientes
 a las tipas (llamalos df_tipas_parques y df_tipas_veredas, respectivamente) y 
 las columnas correspondientes al diametro a la altura del pecho y alturas. 
 
 Hacelo  como copias (usando .copy() como hicimos más arriba) para poder trabajar 
 en estos nuevos dataframes sin modificar los dataframes grandes originales. 
 
 Renombrá las columnas que muestran la altura y el diámetro a la altura del pecho
 para que se llamen igual en ambos dataframes, para ello explorá el comando rename.
"""
import pandas as pd
df_veredas=pd.read_csv(r'../Data/arbolado_lineal.csv')
df_parques=pd.read_csv(r'../Data/arbolado.csv')

# 'Tipuana tipu' in df_veredas['nombre_cientifico'].unique() 
# 'Tipuana Tipu' in df_parques['nombre_cie'].unique()

df_tipas_parques= df_parques[df_parques['nombre_cie']=='Tipuana Tipu'].copy()
df_tipas_parques=df_tipas_parques[['altura_tot','diametro']]

df_tipas_veredas= df_veredas[df_veredas['nombre_cientifico']=='Tipuana tipu'].copy()
df_tipas_veredas=df_tipas_veredas[['altura_arbol','diametro_altura_pecho']]

nombres_cols=dict(zip(df_tipas_parques.columns,df_tipas_veredas.columns))
df_tipas_parques.rename(columns=nombres_cols, inplace=True)


'''
Agregale a cada dataframe (df_tipas_parques y df_tipas_veredas) una columna 
llamada 'ambiente' que en un caso valga siempre 'parque' y en el otro caso 'vereda'.
'''
df_tipas_parques['ambiente']='parque'
df_tipas_veredas['ambiente']='vereda'


'''
Juntá ambos datasets con el comando 
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques]). 
De esta forma tenemos en un mismo dataframe la información de las tipas 
distinguidas por ambiente.
'''
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
df_tipas.boxplot('diametro_altura_pecho',by = 'ambiente')
df_tipas.boxplot('altura_arbol',by = 'ambiente')


# =============================================================================
# 
# idea para una función/paquete futuro:
#     
#     una función que toma dos dataframes y dos nombres de columnas, devuelve el
#     segundo dataframe renombrado como el primero
#     
#     un buscador de caracteres del tipo tiene_a(palabra) que contemple mayúsculas
#     minusculas y caracteres especiales, que tome dos dataframes, la columna a mirar
#     y la palabra que buscamos y devuelva de cada dataframe la o las palabras 
#     coincidentes con la entrada en cada df. Apunto a algo así:
#         
#         coincidencia(df_veredas, df_parques, 'tipuana tipu')
#         >>> ['Tipuana tipu', 'Tipuana Tipu']
#     
#     con todo esto podría armar una función que dados los dos dataframes y una especie
#     haga toda la conversión de nombres de columnas, busque coincidencias, arme
#     el dataframe mergeado (y talvez lo devuelva) y plotee en función de diámetro
#     y altura.
#     esto incluso se puede iterar para varias especies
#
# =============================================================================
