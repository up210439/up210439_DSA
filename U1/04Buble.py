# AUTOR: MARIA DEL CARMEN VIRAMONTES CONTRERAS 
# EJERCICI0: BUBLE
# FECHA: 10 DE FEBRERO DEL 2023 
# CORREO: up210439@alumnos.upa.edu.mx


lista= [4,22,13,16,8]
swapped = True
print("The list is not ordered", lista)
while swapped:
    swapped = False
    for i in range (len(lista) -1):
        if lista[i] > lista[i+1]:
            swapped=True
            lista[i], lista[i+1] = lista[i+1], lista[i]

print("The list is ordered ", lista)