
#Resolución del problema de la mochila con programación dinámica: memoization

def solve_memoization(items, capacity):

    memo = {}    #Diccionario utilizado como memoria
    value = 0
    taken = [0] * len(items)
    n = len(items)-1

    def getKey(n, c):
        return str(n) + " " + str(c)

    #Fase1
    def memoization(n, c):
        key = getKey(n,c)

        #Caso base
        if n<0 or c==0:
            return 0

        #Si el caso a comprobar ya se encuentra en la memoria no hay que volver a comprobarlo
        if key in memo:
            return memo[key]

        #Si el caso es válido se debe estudiar si se coge o no, en caso contrario se pasa al siguiente
        if items[n].weight <= c:
            a = items[n].value + memoization(n-1, c-items[n].weight)
            b = memoization(n-1, c)
            memo[key] = max(a, b)
            return memo[key]
        else:
            memo[key] = memoization(n-1, c)
            return memo[key]

    value = memoization(n, capacity) #De la Fase 1 se obtiene el parámetro value del resultado

    v = value;
    k=n
    #Fase2
    #De esta segunda fase se obtiene el parámetro taken del resultado comprobando la memoria
    while k >= 0 and capacity > 0 :
        if k != 0:
            x = getKey(k, capacity)
            y = getKey(k-1, capacity)
            if memo[x] != memo[y]:
                taken[k] = 1
                capacity -= items[k].weight
                v -= items[k].value
        else:
            z = getKey(k, capacity)
            if memo[z] >= v and items[k].weight <= capacity:
                taken[k] = 1
        k -= 1;
    return value, taken