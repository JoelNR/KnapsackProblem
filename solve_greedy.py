
from random import randint
#Función de ordenación randomizada para Greedy        
def QuickSort(items, inDesiredOrder):
    start = items[0].index
    end = len(items)-1
    
    def qs(items, start, end):
        if (inDesiredOrder(end, start)):
            piv_pos = partition(items,start,end)
            qs(items, start, piv_pos - 1)   #Llamadas recursivas para ordenar los sub-arrays
            qs(items, piv_pos + 1, end)
        
    def partition(items, start, end): 
        i = start
        rand = randint(start, end-1)
        pivot = items[rand]             #Se elige el pivote de manera aleatoria => Randomized QuickSort
        items[end], items[rand] = items[rand], items[end]   #Se envia el pivote al final
        for j in range(start, end):
            #Se comprueba varios casos significativos para los datos de entrada y se van moviendo
            # y ordenando los items según el orden deseado (función lambda)
            if len(items) > 30:
                if (not inDesiredOrder((pivot.value/pivot.weight), (items[j].value/items[j].weight))):
                    items[i], items[j] =  items[j], items[i]
                    i += 1
            else:
                if (inDesiredOrder((pivot.value/pivot.weight), (items[j].value/items[j].weight))):
                    items[i], items[j] =  items[j], items[i]
                    i += 1
        items[i], items[end] = items[end], items[i]
        return (i)
        
    return qs(items, start, end)

  
def solve_greedy(items, capacity):
    value  = 0
    weight = 0
    taken  = [0]*len(items)
    QuickSort(items, lambda x, y: x > y) #Llamada a la función de ordenación con función lambda
    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value  += item.value
            weight += item.weight
    return value, taken