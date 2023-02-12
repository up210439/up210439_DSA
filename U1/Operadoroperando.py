# AUTOR: MARIA DEL CARMEN VIRAMONTES CONTRERAS 
# EJERCICI0: Operador operando (infix y posfix)
# FECHA: 07 DE FEBRERO DEL 2023 
# CORREO: up210439@alumnos.upa.edu.mx

''' 07 de febrero del 2023 
INFIX = 5 * (6+2) - 12 / 4 =37
POSFIX = 5 6 2 + * 12 4 / - para resolver este método, vas tomando los signos por orden. al tomar el primer signo 
                            se tiene que tomar los dos ultimos números, por ejemplo. (5 6 2 +) se toma el 6 y 2 
                            entonces se toma en cuenta en signo (+), despues se toma la multiplicación porque 
                            es la que sigue y se toman como numeros el 5 y el resultado 8 que fue (6+2=8) = 40
                            despues se toma división de 12/4 y para finalizar se toma 40 y 3 (12/4=3) =37


'''
def prioridad (c):
#p = ['+','-','*','/','^','()']
#la numeración comienza de 4 dandole el valor más bajo, El 1 es el valor más alto.

    if c in ['+', '-']:
        return 4 
    elif c in ['*', '/']:
        return 3
    elif c in ['^']:
        return 2
    elif c in ['()']:
        return 1 

p = ['5','6','2','+','*','12','4','/','-']
p.append(')')
stack = [] #pila 
value = 0 #resultado de la pila 
contador = 0 #posicion 
p1 = 0 #B
p2 = 0 #A

while (p[contador] != ')'): #si es diferente a ) entonces entra al ciclo 
   
    if (p[contador]== '+'):
        p1 = stack.pop()
        p2 = stack.pop()
        c = p2 + p1
        stack.append(c)
        print("prioridad del operador es:", (p[contador]), prioridad(p[contador]))
    elif (p[contador]== '-'):
        p1 = stack.pop()
        p2 = stack.pop()
        c = p2 - p1
        stack.append(c)
        print("prioridad del operador es:", (p[contador]), prioridad(p[contador]))
    elif (p[contador]== '*'):
        p1 = stack.pop()
        p2 = stack.pop()
        c = p2 * p1
        stack.append(c)
        print("prioridad del operador es:", (p[contador]), prioridad(p[contador]))
    elif (p[contador]== '/'):
        p1 = stack.pop()
        p2 = stack.pop()
        c = p2 / p1
        p2.append(c)
        print("prioridad del operador es:", (p[contador]), prioridad(p[contador]))
    elif (p[contador]== '**'):
        p1 = stack.pop()
        p2 = stack.pop()
        c = p2 ** p1
        stack.append(c)
        print("prioridad del operador es:", (p[contador]), prioridad(p[contador]))
    else:
        stack.append(int(p[contador]))
    
    contador += 1

value = stack[-1]

print(value) 

'''
prioridades: tiene mayor prioridad () 
+ - es la prioridad más baja 
* / es la prioridad media 
^ es la prioridad alta 
() es la prioridad más alta 

'''

