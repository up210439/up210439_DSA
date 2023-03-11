def mover_al_principio(parametros, n):
    # Tomar los últimos n elementos de la lista original
    ultimos_elementos = parametros[-n:]
    
    # Concatenar los últimos elementos con el resto de la lista
    nueva_lista = ultimos_elementos + parametros[:-n]
    
    return nueva_lista

parametros = [1, 2, 3, 4, 5]
n = 2

nueva_lista = mover_al_principio(parametros, n)
print(nueva_lista)



