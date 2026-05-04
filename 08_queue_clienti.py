'''
Simula la fila di clienti dal macellaio.
1. Arrivano in ordine: "Mario", "Giulia", "Tonino", "Rosa"
2. Il macellaio chiama il primo cliente — stampa: "Servo: Mario"
3. Arriva un nuovo cliente: "Enzo"
4. Stampa quante persone sono ancora in fila
5. Servi tutti i clienti rimanenti fino a chiusura

'''
from collections import deque

class Queue:
    def __init__(self):
        self.__data=deque() 

    def enqueue(self,item):
        self.__data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Nessun cliente in coda.")
        return self.__data.popleft() 
    
    def peek(self):
       if self.isEmpty():
            raise IndexError("Nessun cliente in coda")
       return self.__data[0] 
    
    def isEmpty(self):
        return len(self.__data)==0
    
    def size(self):
        return len(self.__data)
    
    def __repr__(self):
        return f"Clienti in coda: ({list(self.__data)})"


coda_clienti = Queue()
clienti_iniziali = ["Mario", "Giulia", "Tonino", "Rosa"]

for cliente in clienti_iniziali:
    coda_clienti.enqueue(cliente)

print('Servo:', coda_clienti.dequeue())

print ('Arriva Enzo')

coda_clienti.enqueue('Enzo')

print ('Persone in fila:', coda_clienti.size())

while not(coda_clienti.is_empty()):
    print('Servo:', coda_clienti.dequeue())
