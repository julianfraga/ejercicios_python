# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 15:49:53 2022

@author: Julián
"""
import random as rn
import numpy as np
def medir_temp(n, temp=37.5, mu=0,sigma=0.2):
    temperaturas=[]
    for i in range(n):
        error=rn.normalvariate(mu, sigma)
        medicion=temp+error
        temperaturas.append(medicion)
    return(temperaturas)

def resumen_temp(n, temp=37.5,mu=0, sigma=0.2):
   
    x=medir_temp(n, temp=temp, mu=mu, sigma=sigma)
    media=sum(x)/n
    x.sort()
    
    def es_par(n):
        if n%2==0:
            return False
        else:
            return True
    if es_par(n):
        mediana=(x[n//2]+x[n//2+1])/2
    else:
        mediana=x[n//2+1]
    np.save(r'.\Data\temperaturas.npy', x)   
    return(max(x), min(x), media,mediana)

resumen_temp(999)     
