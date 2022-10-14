# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 11:28:09 2021

@author: Usuario
"""

import sys
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from math import *
df = pd.read_csv("glass_dataset.csv")
column=len(df.axes[1])
kmeans=KMeans(n_clusters=6)
clusters=kmeans.fit_predict(df) 
try:
    archivo=open("glass_dataset.csv")
    lineas=archivo.readlines()
    archivo.close()
except IOError:
    print('No se pudo abrir el archivo')
    sys.exit(1)
n=len(lineas)
grupos=[]
for i in kmeans.cluster_centers_:
    print(i)
def calcularDistanciaEuclidiana(lineas,i):
    suma=0
    for i in range(n):
        suma=suma+pow(lineas[i]-i[i],2)
        print(suma)
    return sqrt(suma)
print("n: ", n)
print("*** CENTROIDES ***")
print(kmeans.cluster_centers_)