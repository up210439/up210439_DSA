def validar_parentesis(cadena):
    parentesis_contador =0
    for elemento in cadena:
        if elemento == "(":
            parentesis_contador +=1
        if elemento == ")":
            parentesis_contador -=1
        if parentesis_contador < 0:
            return False
    #Todo valor que sea != 0 por defaault son condiciones = True  
    return not parentesis_contador 

if __name__ == "__main__":
    print(validar_parentesis("(a(b*c(d))"))


#casos para verificar 
#(), )(), ))(), ()(), ()(, (())((()))(()), (())((()))((), (a(b*c(d))), (a(b*c(d))

'''
cuando el valor final es 0 entonces es True, siempre y cuando no sea negativo. entonces se niega en 0 para tomarlo como TRUE
y pasar todos los demás numeros a False. 

'''