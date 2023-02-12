# AUTOR: MARIA DEL CARMEN VIRAMONTES CONTRERAS 
# EJERCICI0: SUMATORIA 
# FECHA: 18 DE ENERO DEL 2023 
# CORREO: up210439@alumnos.upa.edu.mx

#Número de boletos 
n = 0

#Sumatoria para saber que cantidad sobra 
suma=int(input("¿Cuanto dinero tienes?"))

while suma > n:
    n += 1 
    suma -= n 

#Resultado 
print("La cantidad de boletos que ajustas es: ", n)
print("Cantidad que te sobra: ", suma)
