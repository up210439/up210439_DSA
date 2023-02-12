# AUTOR: MARIA DEL CARMEN VIRAMONTES CONTRERAS 
# EJERCICI0: MATRIZ SIN REPETIDOR  
# FECHA: 10 DE FEBRERO DEL 2023 
# CORREO: up210439@alumnos.upa.edu.mx

from random import randrange
p = int(input("Escoge el tamaño de la matriz: "))
lista = [[0 for j in range(p)] for i in range(p)]
fila = 0
columna = 0
while fila < p:
    igual = False
    a = randrange(1, ((p**2) + 1))
    for fila1 in range(p):
        for columna1 in range(p):
            if (lista[fila1][columna1] == a):
                igual = True
    if igual == False:
        lista[fila][columna] = a
        columna = columna + 1
        if columna == p:
            columna = 0
            fila = fila + 1
print(lista)


