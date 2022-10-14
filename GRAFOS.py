# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 02:13:46 2021

@author: User
"""

import sys

m=0
grados=[]

try:
    archivo=open(sys.argv[1])
    lineas=archivo.readlines() #Lee filas
    archivo.close()
except IOError:
    print('No se pudo abrir el archivo')
    sys.exit(1)
    
#n = Numero de vertices
n=len(lineas)


#linea=lineas[0]  Imprime la 1° Fila
#print(linea.strip())  Acomoda con tab
#print(linea.split())  Delimita con comas

for linea in lineas:
    linea=linea.strip()
    celdas=linea.split()
    grado=0
    for celda in celdas:
        m+=int(celda)
        grado+=int(celda)
    grados.append(grado)
        
#m = Numero de aristas
m=m/2

densidad=2*m/(n*(n-1))

print("n: ", n)
print("m: ", m)
print("Densidad: ", round(densidad,3))
print("")



#Lista de grados
for i in range(len(grados)):
    print("Grado v"+str(i)+"="+str(grados[i]))
    
    centralidad=grados[i]/(n-1)
    
    print("Centralidad v"+str(i)+"="+str(centralidad))
    print("")





