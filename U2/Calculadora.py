# AUTOR: MARIA DEL CARMEN VIRAMONTES CONTRERAS 
# EJERCICI0: Calculadora 
# FECHA: 10 de Marzo del 2023 
# CORREO: up210439@alumnos.upa.edu.mx

import tkinter as tk
import math 


''' 07 de febrero del 2023 
INFIX = 5 * (6+2) - 12 / 4 =37
POSFIX = 5 6 2 + * 12 4 / - para resolver este método, vas tomando los signos por orden. al tomar el primer signo 
                            se tiene que tomar los dos ultimos números, por ejemplo. (5 6 2 +) se toma el 6 y 2 
                            entonces se toma en cuenta en signo (+), despues se toma la multiplicación porque 
                            es la que sigue y se toman como numeros el 5 y el resultado 8 que fue (6+2=8) = 40
                            despues se toma división de 12/4 y para finalizar se toma 40 y 3 (12/4=3) =37


'''
operadores = ['+', '-', '/', '*', '(', ')', '^','sen','tan','cos','asin','acos','atan','ln','log']
funciones = ['sen','tan','cos','asen','acos','atan','ln','log']

def prioridad(c):
    if c in ['+', '-']: #bajo
        return 1 
    elif c in ['*', '/']: #bajo
        return 2
    elif c in ['^']: #alto
        return 3
    elif c in ['(',')']: #alto
        return 0 


n = ["5","*","(","6","+","2",")","-","12","/","4"]
n.append(')')
n.insert(0,'(')

def infix_posfix(n):
    p = []
    stack = []

    for i in n:
        if i not in ['+','-','/','*','(',')']:
            p.append(i)
        elif i == '(':
            stack.append(i)
        elif i in ['+', '-', '/', '*']:
            contador = len(stack)-1
            while prioridad(stack[contador]) >= prioridad(i):
                    p.append(stack.pop())
                    contador-=1
            stack.append(i)
        elif i == ')':
            contador = len(stack) - 1
            while stack[contador] != '(':
                p.append(stack.pop())
                contador-=1
            stack.pop()
    p.append(')')
    return p

def operacion(operacion):  
    stack = []
    for i in operacion:
        if i not in ['+','/','-','*','^',')','^','sen','tan','cos','asen','acos','atan','ln','log']:
            numero = float(i)
            stack.append(numero)
        else:
            match (i):
                case '+':
                    b = stack.pop()
                    a = stack.pop()
                    c = a + b
                    stack.append(c)
            
                case '-':
                    b = stack.pop()
                    a = stack.pop()
                    c = a - b
                    stack.append(c)
                   
                case '*':
                    b = stack.pop()
                    a = stack.pop()
                    c = a * b
                    stack.append(c)
                    
                case '/':
                    b = stack.pop()
                    a = stack.pop()
                    c = a / b
                    stack.append(c)
                    
                case '^':
                    b = stack.pop()
                    a = stack.pop()
                    c = a ** b
                    stack.append(c)
                case 'sen':
                    Y = math.sin(math.radians(stack.pop()))
                    stack.append(Y)
                case 'cos':
                    Y = math.cos(math.radians(stack.pop()))
                    stack.append(Y)
                case 'tan':
                    Y = math.tan(math.radians(stack.pop()))
                    stack.append(Y)
                case 'asen':
                    Y = math.degrees(math.asin(stack.pop()))
                    stack.append(Y)
                case 'acos':
                    Y = math.degrees(math.acos(stack.pop()))
                    stack.append(Y)
                case 'atan':
                    Y = math.degrees(math.atan(stack.pop()))
                    stack.append(Y)
                case 'ln':
                    Y = stack.pop()
                    stack.append(math.log(Y))
                case 'log':
                    Y = stack.pop()
                    Z = stack.pop()
                    stack.append(math.log(Y,Z))
                case ')':
                    break
                case _:
                    break   
                
    value = stack.pop()
    return value
def enlistar(n):
    op=[]
    a =''
    for i in n:
        if i not in ['+','-','/','*','(',')','^']:
            a +=i
        else:
            if a!='':
                op.append(a)
            op.append(i)
            a = ''
    if a != '':
        op.append(a)

    return op
def operacion_Final(op):
    a = enlistar(op)
    b = infix_posfix(a)
    c = operacion(b)
    return c
'''
prioridades: tiene mayor prioridad () 
+ - es la prioridad más baja 
* / es la prioridad media 
^ es la prioridad alta 
() es la prioridad más alta 

'''


class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        # Crear la caja de texto
        self.display= tk.Entry()
        self.display = tk.Text(master, width=25, height=2, background = "orange", foreground = "snow", font=("Helvetica", 20))
        self.display.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
    

        # Crear los botone
        'sen','tan','cos','asen','acos','atan','ln','log'

        boton_sin = self.crear_boton("sen", 1,0)
        boton_cos = self.crear_boton("cos", 1,1)
        boton_tan = self.crear_boton("tan", 1,2)
        boton_asin = self.crear_boton("asen", 1,3)
        boton_acos = self.crear_boton("acos", 1,4)
        
        boton_atan = self.crear_boton("atan", 2,0)
        boton_in = self.crear_boton("ln", 2,1)
        boton_alog = self.crear_boton("log", 2,2)
        boton_potencia = self.crear_boton("^", 2,3)
        
        boton7 = self.crear_boton("7", 3, 0)
        boton8 = self.crear_boton("8", 3, 1)
        boton9 = self.crear_boton("9", 3, 2)
        #----------boton borrar -----------------

        boton4 = self.crear_boton("4", 4, 0)
        boton5 = self.crear_boton("5", 4, 1)
        boton6 = self.crear_boton("6", 4, 2)
        boton_mul = self.crear_boton("*", 4, 3)
        boton_division = self.crear_boton(u"\u00F7", 4, 4)
        
        
        boton1 = self.crear_boton("1", 5, 0)
        boton2 = self.crear_boton("2", 5, 1)
        boton3 = self.crear_boton("3", 5, 2)
        boton_resta = self.crear_boton("-", 5, 3)
        boton_suma = self.crear_boton("+", 5, 4)

        boton0 = self.crear_boton("0", 6, 0)
        boton_punto = self.crear_boton(".", 6, 1)
        boton_igual = self.crear_boton("=", 6,2)
        boton_izquierdo = self.crear_boton("(", 6, 3)
        boton_derecho = self.crear_boton(")", 6, 4)
        
        # Crear el botón de borrado 
        boton_borrar = tk.Button(master, text=u"\u232B", width=17, height=3, command=lambda: self.borrar)
        boton_borrar.grid(row=3, column=3, columnspan= 2, padx=5, pady=5)

    #botones 
    def crear_boton(self, texto, fila, columna):
        boton = tk.Button(self.master, text=texto, width=6, height=3, command=lambda: self.pulsar(texto))
        boton.grid(row=fila, column=columna, padx=5, pady=5)
        return boton
    
    def pulsar(self, tecla):
        if tecla == "=":
            resultado=self.display.get()
            #funcion de agregar espacios
            self.resultado=self.enlistar(resultado)
            resultado = infix_posfix(resultado)
            resultado=operacion(resultado)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(resultado))
        elif tecla == u"\u232B":
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, tecla)

    def borrar(self):
        self.display.delete(0, tk.END)
    

root = tk.Tk()
mi_calculadora = Calculadora(root)
root.mainloop()
