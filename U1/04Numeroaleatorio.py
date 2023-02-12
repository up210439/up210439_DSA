# AUTOR: MARIA DEL CARMEN VIRAMONTES CONTRERAS 
# EJERCICI0: NÚMERO ALEATORIO 
# FECHA: 01 DE FEBRERO DEL 2023 
# CORREO: up210439@alumnos.upa.edu.mx

#Librería matematica 

import random
mi_list = []

Fin=30 
for i in range(1, Fin+1):
    mi_list.append(random.randint(0, 20))
    unicos = list(dict.fromkeys(mi_list)) #Se generara un nuevo diccionario números validos únicos. 
#print('Con duplicados',  mi_list)
print()    
print('Unicos',unicos) 
