# AUTOR: MARIA DEL CARMEN VIRAMONTES CONTRERAS 
# EJERCICI0: POSFIX 
# FECHA: 10 DE FEBRERO DEL 2023 
# CORREO: up210439@alumnos.upa.edu.mx

def prioridad (c):
#p = ['+','-','*','/','^','()']
#la numeración comienza de 4 dandole el valor más bajo 
    if c in ['+', '-']:
        return 4 
    elif c in ['*', '/']:
        return 3
    elif c in ['^']:
        return 2
    elif c in ['()']:
        return 1


'''
Esta función la agregue al proyecto Operador operando 

'''
    

       
