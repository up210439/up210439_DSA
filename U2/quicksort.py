'''
ordenación o busqueda 
memoria estatica o dinamica 

dia 3 de marzo entrega de calculadora 
cual es el costo, ventajas y desventajas (reporte)
método 
inserccion
seleccion
monticulo
fusión Shell 
Quicksort 
que significan, para que sirven, 

'''
'''
Quicksort: rapido para datos pequeños.
hace el programa de una lista de 500 numeros aleatorios y busque el numero dado 
calculadora 

'''
def quicksort(a, i, j):
    PRIN = i
    FIN = j
    central = (i + j )//2
    pivote = a[central]
    while i <= j: 
        while a[i] < pivote:
            i += 1
        while a[j] > pivote:
            j -= 1
        if a[j] <= a[i]: 
             tmp = a[i]
             a[i] = a[j]
             a[j] = tmp 
             i = i + 1
             j = j - 1

    if PRIN < j:
        quicksort(a, PRIN, j)
    if i < FIN:
        quicksort(a, i, FIN)
    return a 
a = [78,21,15,90,65,75,85,76,46,84,74]
i = 0
j = len(a) -1
print(a)
print(quicksort(a,i,j))

    