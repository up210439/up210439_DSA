class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getData(self): #crear funcion 
        return self.data
    
class Stack:
    def __init__(self): 
        self.head = None 
        self.size = 0
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return True if self.size == 0 else False 
        #return True if not self.size else False
        #return True if not self.head else False  
    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head 
        self.head = newNode
        self.size += 1
    def pop(self):
        if self.isEmpty() == False: #checar que la pila no este vacia 
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data 
        return None
    def peak(self): #viendo quien esta en la cima 
        if self.isEmpty() == False:
            data = self.head.data
            return data
        return None
    def show(self): #Mostrar todo lo que tiene la pila 
        cadena = ""

        while self.isEmpty() == False:
            cadena += self.head.data 
            self.head = self.head.next
            self.size -= 1
        return cadena 
'''
pop
push
show 
content 
'''

q1 = Stack() 
q1.push("Jesús")
q1.push("María")
q1.push("José")
print(q1.show())


print("Sacar")
print(q1.pop())
print(q1.pop())
print(q1.pop())
print(q1.pop())

''''
q2 = Stack()
print(q1)
print(q1.head) 
print(q1.getSize())
print(q1.isEmpty())



print(q1)
print(q1.head) 
print(q1.getSize())
print(q1.isEmpty())
print(q1.pop())
print(q1.peek())
'''