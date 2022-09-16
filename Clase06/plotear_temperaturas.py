# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 16:46:09 2022

@author: Julián
"""
import matplotlib.pyplot as plt
import numpy as np
path=r'.\Data\temperaturas.npy'
temperaturas=np.load(path)
plt.clf()
plt.hist(temperaturas,bins=25)
plt.xlabel('Temperatura (ºC)')
plt.show()