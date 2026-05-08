'''
Coda di messaggi in chat
Simula una coda di messaggi in arrivo.
Arrivano in ordine: "ciao!", "come stai?", "ci sei?"
Processa il primo messaggio — stampa: "Nuovo messaggio: ciao!"
Arriva un nuovo messaggio: "ok dai ci sentiamo dopo"
Stampa quanti messaggi sono ancora in attesa
Processa tutti i messaggi rimanenti fino a quando la coda è vuota
'''
from collections import deque

class Queue:
    def __init__(self):
        self.__data=deque() 

    def enqueue(self,item):
        self.__data.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Nessun messaggio.")
        return self.__data.popleft() 
    
    def peek(self):
       if self.isEmpty():
            raise IndexError("Nessun messsagio.")
       return self.__data[0] 
    
    def isEmpty(self):
        return len(self.__data)==0
    
    def size(self):
        return len(self.__data)
    
    def __repr__(self):
        return f"Messaggi:{list(self.__data)}"

coda_messaggi = Queue()
coda_messaggi.enqueue("ciao!")
coda_messaggi.enqueue("come stai?")
coda_messaggi.enqueue("ci sei?")
    
print(f'Hai {coda_messaggi.size()} nuovi messaggi!')

print(coda_messaggi.dequeue())
coda_messaggi.enqueue("ok dai ci sentiamo dopo")
print("È arrivato un nuovo messaggio!")
print(f'Hai {coda_messaggi.size()} nuovi messaggi!')
while not coda_messaggi.isEmpty():
    print(coda_messaggi.dequeue())
