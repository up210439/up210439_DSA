class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getData(self): #crear funcion 
        return self.data
    
    def setData(self, dato):#atributos de la función 
        self.data = dato
    
nodo1 = Node("Jesus")
print(nodo1.data)
print(nodo1.getData())
print(nodo1.next) 

nodo1.setData("Maria")
print(nodo1.getData())
print(nodo1.data)

nodo2 = Node ("José")
nodo1.next = nodo2

nodo3 = Node ("Jesús")
nodo2.next = nodo3 #se agrega la dirección de nodo3 al nodo2

print("+++++++++++++++++++++++++++++++")#poner atención desde aquí 
print(nodo1.data)
print(nodo1.next.data)
print(nodo1.next.next.data)
print(nodo1,next.next.next)






     
    