# AUTOR: MARIA DEL CARMEN VIRAMONTES CONTRERAS 
# EJERCICI0: NÚMERO SECRETO
# FECHA: 17 DE ENERO DEL 2023 
# CORREO: up210439@alumnos.upa.edu.mx

'''
Buscar una libreria que haga números al hazar, teclear número secreto que al poner
el número si el número es bajo "más o subele " o si es alto "menos o bajale", al 
dar con el número "bingo " TAREA 02SecretNumber. Poner un contador (para checar los intentos)

'''

numero_Secreto = 16
num = 0
contador = 0

while num != numero_Secreto:
    num = int(input("Teclea un número :D "))
    if num < numero_Secreto:
        print("Casi pero no + súbele :( ")
    elif num > numero_Secreto:
        print("Ups muy alto - bájale ")
    else:
        print("¡Eale! ES TODO =>> LE DISTE AL GORDO SUERTUDOTE ")
        print("COME FRUTAS Y VERDURAS")
