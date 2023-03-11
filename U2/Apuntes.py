horas= 12
minutos= 17
duracion= 59
finalizar= 13.16
#finalizacion= 13:16

#Determinar horas 
horas = horas + ((minutos + duracion) //60)

#Reciduo de 24 para que no sobre pase las 24 hrs y regrese.
horas = horas %24

#Determinar minutos 
minutos = (minutos + duracion) % 60 

#Imprimir el tiempo en horas en total 
print ("El tiempo es =>", horas, ":", minutos,"Hrs")
print ("Hora:", horas, "Hr")
print ("minutos:", minutos, "min")

a = 4
b = 16
c = 3

#**************************************************
##if a > b: 
#   a = a
#elif b > a:
#    a = b
#elif a > c:
#   a = c
#else 

#**************************************************
'''
matricula_DSA nombre de la carpeta 
U1,U2,U3,U4
01Biseccion.py
carlosherrerah/matricula 
'''


#*************************************************
#Modulo 3

#igualar   
a = 1 == 1 #True
print(a)

#diferente 
a = 0 
print (a != 0) #False

'''
parentesis duplas 
corchetes lista
type muestra que tipo de variable estamos utilizando 

'''
#objetivo: if, elif y else 
#leap year

year = int (input("¿How many days have the year?: "))

#Si el año es menor a 1582, entonces no es un año gregoriano
if year < 1582:
    print("Not within the Gregorian calendar period: ") #El calendario no es gregoriano
elif (year % 4) != 0: 
    print("The result is common year ")
elif (year % 100) != 0: 
    print("The result is leap year ")
elif (year % 400) != 0:
    print("The result is common year ")
else:
    print("The result is leap year ")


#CICLO INFINITO

ciclo_Infinito = 0
while ciclo_Infinito == 0:
    print("Papas fritas jas jas ")

'''

while true:
    print("Hello")

'''

#Cuando una variable es != 0 es TRUE y cuando la variable es igial a 0 es FALSO 

'''
Buscar una libreria que haga numeros al hazar, poner numero secreto que al poner
un numero el usuario y es bajo "mas o subele " o si es alto "menos o bajale", al 
dar con el número "bingo " TAREA 02SecretNumber. Poner un contador (para checar los intentos)

'''

'''
Para cambiar un valor a otro 
a= 5
b=6
    a,b=b,a

'''
'''
pass para que lo uso: no hce nada 

if edad < 18:
    pass #no hace nada 
else: 
    aqui da a enterder que si es mayor a 18 y pide datos 

diferencia en continuo y el break
continuo: se regresa al inicio, no se sale del ciclo  
break: se va para abajo, se sale del ciclo 

in dentro de un for (mandar un elemento uno por uno) se entiende por que es un ciclo 
cuando esta dentro de un if es porque esta checando (si es verdad o falso) solamente 
letter in user_word= es que letter esta dentro de user_word (es parte de la variable)

not in = es diferente de(variable)

'''
#Example: word without vowels
user_word = input("Gime a Word: ")
user_word = user_word.upper()
new_word = ""
for letter in user_word:
    if letter not in ("A","B","C","D","E","F","G","H"):
        new_word += letter 
print(new_word)

#HIPOTESIS
c0 = 16

c0 = input("Give a number")

if c0 > 0:
   while c0 % 2 == 0: #Si es par
    c0 = c0/2 
    print(c0)
else:
    c0 = 3*c0 +1  #Impar
     
    print(c0)

#SECCION 3.3
'''
AND = CONJUNCION ^ multiplicacion 
OR = DISJUNCION v   suma 
& = AND
|| = OR
~ = NEGACION 
corrimientos multiplicar o dividir
print(i>>3)  multiplica por 2 
print(i<<3) divide por 2
'''

#ordena 
    #numbers.sort()
#remove quita el valor(pero deja la posicion) y del quita la posición (se recorre)
#append al final numbers.append(13) es el valor que va agregar al final de la fila 
#numbers.insert(3,33) en la posicion 3 se mete el 33 (es un colado jajaj)


#VECTORES ORDENA
#import numpy as np (libreria, se requiere imprimir)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers.sort() #una forma de hacerlo 
ordenado=sorted(numbers) #lo mismo pero más codigo 
print(ordenado)
print(numbers) 

'''
pop (quita el ultimo digito)

El punto despues de las variables lo toma como objeto (regresa el valor de la variable 
que estas igualando)


'''

name = "Universidad"
r = name.replace("sida" , "vih")
print(r)

my_list = [] 
suma = 0
for i in range(5):
    my_list.append((i + 1)*10) #el valor lo pone como en fila, ordenamiento 
    #my_list.insert(0, (i+1)*10) => esta funcion pone el valor al principio independientemete quien este en la posicion 0,0
    #el primer valor queda al final 
    suma += my_list[i]
print(my_list)
print(suma)
#print(np.sum(my_list))

'''
#swap
a = 5
b = 6
a,b = b,a
print(a,b)

a = [10, 20, 30, 40, 50]
suma = 0 
for i in range(5):
    v = i + 1 * 10
    a [0, (v)]
    suma += a [i]
print(a)
print(suma)

'''

nombre = "Universidad Politécnica"
print(nombre[6:10]) #imprime las posiciones que dan de 6 a 10 que son sida
x = nombre.split()
print(x[1]) 



# AUTOR: MARIA DEL CARMEN VIRAMONTES CONTRERAS 
# EJERCICI0: APUNTES 
# FECHA: 14 DE FEBRERO DEL 2023 
# CORREO: up210439@alumnos.upa.edu.mx
'''
Q = ( A + ( B * C - ( D / E ^ F ) * G ) * H )
P = A B C * D E F ^ / G * - H * + 
STACK

''' 