'''
Usa la classe LinkedList per gestire una lista di numeri.
Inserisci in ordine: 10, 20, 30
Stampa la lista
Inserisci 25 dopo 20
Stampa la lista
Inserisci 5 prima di 10 — caso speciale, è la testa
Stampa la lista
Inserisci 15 prima di 20
Stampa la lista
Rimuovi il primo elemento
Stampa la lista
Rimuovi l'ultimo elemento
Stampa la lista
Stampa quanti elementi sono nella lista
Stampa il primo elemento senza rimuoverlo

'''
class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.next   = None

class LinkedList:
    def __init__(self):
        self.__testa = None
        self.__size  = 0

    def insertFirst(self, valore):
        nuovo        = Nodo(valore)
        nuovo.next   = self.__testa
        self.__testa = nuovo
        self.__size += 1

    def insertLast(self, valore):
        nuovo = Nodo(valore)
        if self.__testa is None:
            self.__testa = nuovo
        else:
            corrente = self.__testa
            while corrente.next is not None:
                corrente = corrente.next
            corrente.next = nuovo
        self.__size += 1

    def insertAfter(self, valore_riferimento, nuovo_valore):
        corrente = self.__testa
        while corrente is not None:
            if corrente.valore == valore_riferimento:
                nuovo         = Nodo(nuovo_valore)
                nuovo.next    = corrente.next
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next
        raise ValueError(f"{valore_riferimento} non trovato nella linked_list")

    def insertBefore(self, valore_riferimento, nuovo_valore):
        if self.isEmpty():
            raise IndexError("linked_list vuota")
        if self.__testa.valore == valore_riferimento:
            self.insertFirst(nuovo_valore)
            return
        corrente = self.__testa
        while corrente.next is not None:
            if corrente.next.valore == valore_riferimento:
                nuovo         = Nodo(nuovo_valore)
                nuovo.next    = corrente.next
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next
        raise ValueError(f"{valore_riferimento} non trovato nella linked_list")

    def removeFirst(self):
        if self.isEmpty():
            raise IndexError("removeFirst da una linked_list vuota")
        valore       = self.__testa.valore
        self.__testa = self.__testa.next
        self.__size -= 1
        return valore

    def removeLast(self):
        if self.isEmpty():
            raise IndexError("removeLast da una linked_list vuota")
        if self.__testa.next is None:
            valore       = self.__testa.valore
            self.__testa = None
            self.__size -= 1
            return valore
        corrente = self.__testa
        while corrente.next.next is not None:
            corrente = corrente.next
        valore        = corrente.next.valore
        corrente.next = None
        self.__size -= 1
        return valore

    def peekFirst(self):
        if self.isEmpty():
            raise IndexError("linked_list vuota")
        return self.__testa.valore

    def isEmpty(self):
        return self.__testa is None

    def size(self):
        return self.__size

    def __repr__(self):
        elementi = []
        corrente = self.__testa
        while corrente is not None:
            elementi.append(str(corrente.valore))
            corrente = corrente.next
        return "LinkedList([" + " → ".join(elementi) + "])"

#Inserisci in ordine: 10, 20, 30
l = [10,20,30]
linked_list = LinkedList()
for i in l:
    linked_list.insertLast(i)

#Stampa la linked_list
print(linked_list)

#Inserisci 25 dopo 20
linked_list.insertAfter(20,25)
print(linked_list) # LinkedList([10 → 20 → 25 → 30])

#Inserisci 5 prima di 10 — caso speciale, è la testa
linked_list.insertBefore(10, 5)
print(linked_list)   # LinkedList([5 → 10 → 20 → 25 → 30])

# Inserisci 15 prima di 20
linked_list.insertBefore(20, 15)
print(linked_list)   # LinkedList([5 → 10 → 15 → 20 → 25 → 30])

# Rimuovi il primo elemento
linked_list.removeFirst()
print(linked_list)   # LinkedList([10 → 15 → 20 → 25 → 30])

# Rimuovi l'ultimo elemento
linked_list.removeLast()
print(linked_list)   # LinkedList([10 → 15 → 20 → 25])

# Stampa quanti elementi sono nella linked_list
print(f"Elementi in linked_list: {linked_list.size()}")    # 4

# Stampa il primo elemento senza rimuoverlo
print(f"Primo elemento: {linked_list.peekFirst()}")  # 10
