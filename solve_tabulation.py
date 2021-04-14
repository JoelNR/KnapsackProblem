import numpy as np

#Resolución del problema de la mochila con programación dinámica: tabulation
def solve_tabulation(items, capacity):
    value = 0
    taken = [0] * len(items)
    c = capacity+1
    n = len(items)+1
    V = np.zeros(shape=(n,c))   #Tabla con ceros
    
    #Fase1
    #Se va rellenando la tabla desde la primera fila y columna
    for i in range (1, n):
        for j in range (1, c):
            if items[i-1].weight <= j:
                if items[i-1].value + V[i-1,j-items[i-1].weight] > V[i-1,j]:
                    V[i,j] = items[i-1].value + V[i-1, j-items[i-1].weight]
                else:
                    V[i,j] = V[i-1,j]
            else:
                V[i,j] = V[i-1,j]
    #Fase 2            
    #Se recorre la tabla desde el final hacia el principio identificando los items elegidos         
    i=n-1
    k=c-1
    while i>0 and k>0:
        if V[i,k] != V[i-1,k]:  #El elemento está en la mochila
            taken[i-1] = 1
            value += items[i-1].value
            k=k-items[i-1].weight
            i = i-1
        else:                   #El elemento no está en la mochila
            i= i-1
            
    return value,taken
