'''
Ogni volta che arriva una notifica sul telefono, appare in cima alle altreSupponiamo che quando è il momento di leggerle, le leggi partendo dall'ultima arrivata, che scompare dalla cima e appare la notifica precedente.

Implementa una classe Notifiche con questi metodi:

- arriva(messaggio) --> Aggiunge una notifica in cima
- leggi()   ---> Rimuove e mostra la notifica in cima
- prossima ()     ----> Mostra la notifica in cima senza rimuoverla

Comportamento atteso:

arriva("WhatsApp: Ciao!")
arriva("Gmail: Hai un nuovo messaggio")
arriva("Instagram: Ti hanno taggato")

prossima()   →  "In cima: Instagram: Ti hanno taggato"

leggi()      →  "Letta: Instagram: Ti hanno taggato"
leggi()      →  "Letta: Gmail: Hai un nuovo messaggio"
leggi()      →  "Letta: WhatsApp: Ciao!"
leggi()      →  "Nessuna notifica."
'''
class Stack:
    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.__data.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("empty stack")
        return self.__data[-1]

    def isEmpty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)

    def __repr__(self):
        return f"Stack({self.__data})"