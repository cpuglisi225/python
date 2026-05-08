

#STACK
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
    

# QUEUE
from collections import deque

class Queue:
    def __init__(self):
        self.__data=deque() #deque privato
    
    def enqueue(self,item):
        self.__data.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Dequeue from empty queue")
        return self.__data.popleft() #rimozione dalla testa
    
    def peek(self):
       if self.isEmpty():
            raise IndexError("Empty queue")
       return self.__data[0] 
    
    def isEmpty(self):
        return len(self.__data)==0
    
    def size(self):
        return len(self.__data)
    
    def __repr__(self):
        return f"Queue({list(self.__data)})"
    
#LINKED LIST
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
    
    def search(self, target):
        corrente = self.__testa
        while corrente:           
            if corrente.valore == target:
                return True
            corrente = corrente.next
        return False

    def __repr__(self):
        elementi = []
        corrente = self.__testa
        while corrente is not None:
            elementi.append(str(corrente.valore))
            corrente = corrente.next
        return "LinkedList([" + " → ".join(elementi) + "])"

# DOUBLY LINKED LIST
class NodoD:
    def __init__(self, valore):
        self.valore = valore
        self.next   = None   # puntatore al nodo successivo
        self.prev   = None   # puntatore al nodo precedente

class DoublyLinkedList:
    def __init__(self):
        self.__testa = None
        self.__coda  = None   # novità rispetto a LinkedList
        self.__size  = 0

    def insertFirst(self, valore):
        nuovo = NodoD(valore)
        if self.isEmpty():
            self.__testa = nuovo
            self.__coda  = nuovo
        else:
            nuovo.next        = self.__testa
            self.__testa.prev = nuovo   # novità: aggiorniamo prev
            self.__testa      = nuovo
        self.__size += 1

    def insertLast(self, valore):
        nuovo = NodoD(valore)
        if self.isEmpty():
            self.__testa = nuovo
            self.__coda  = nuovo
        else:
            nuovo.prev       = self.__coda
            self.__coda.next = nuovo    # novità: usiamo __coda direttamente — O(1)
            self.__coda      = nuovo
        self.__size += 1

    def insertAfter(self, valore_riferimento, nuovo_valore):
        corrente = self.__testa
        while corrente is not None:
            if corrente.valore == valore_riferimento:
                if corrente == self.__coda:
                    self.insertLast(nuovo_valore)
                    return
                nuovo              = NodoD(nuovo_valore)
                nuovo.next         = corrente.next
                nuovo.prev         = corrente          # novità: aggiorniamo prev
                corrente.next.prev = nuovo             # novità: aggiorniamo prev del successivo
                corrente.next      = nuovo
                self.__size += 1
                return
            corrente = corrente.next
        raise ValueError(f"{valore_riferimento} non trovato nella lista")

    def insertBefore(self, valore_riferimento, nuovo_valore):
        if self.isEmpty():
            raise IndexError("lista vuota")
        if self.__testa.valore == valore_riferimento:
            self.insertFirst(nuovo_valore)
            return
        corrente = self.__testa
        while corrente is not None:
            if corrente.valore == valore_riferimento:
                nuovo              = NodoD(nuovo_valore)
                nuovo.next         = corrente
                nuovo.prev         = corrente.prev     # novità: aggiorniamo prev
                corrente.prev.next = nuovo             # novità: aggiorniamo next del precedente
                corrente.prev      = nuovo
                self.__size += 1
                return
            corrente = corrente.next
        raise ValueError(f"{valore_riferimento} non trovato nella lista")

    def removeFirst(self):
        if self.isEmpty():
            raise IndexError("removeFirst da una lista vuota")
        valore = self.__testa.valore
        if self.__testa == self.__coda:
            self.__testa = None
            self.__coda  = None
        else:
            self.__testa      = self.__testa.next
            self.__testa.prev = None               # novità: aggiorniamo prev
        self.__size -= 1
        return valore

    def removeLast(self):
        if self.isEmpty():
            raise IndexError("removeLast da una lista vuota")
        valore = self.__coda.valore
        if self.__testa == self.__coda:
            self.__testa = None
            self.__coda  = None
        else:
            self.__coda      = self.__coda.prev    # novità: usiamo __coda direttamente — O(1)
            self.__coda.next = None
        self.__size -= 1
        return valore

    def peekFirst(self):
        if self.isEmpty():
            raise IndexError("lista vuota")
        return self.__testa.valore

    def peekLast(self):                            # novità rispetto a LinkedList
        if self.isEmpty():
            raise IndexError("lista vuota")
        return self.__coda.valore

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
        return "DoublyLinkedList([" + " ⟷ ".join(elementi) + "])"
    
# CIRCULAR LIST
class NodoC:
    def __init__(self, valore):
        self.valore = valore
        self.next   = None

class CircularLinkedList:
    def __init__(self):
        self.__testa = None
        self.__coda  = None
        self.__size  = 0

    def insertFirst(self, valore):
        nuovo = NodoC(valore)
        if self.isEmpty():
            self.__testa = nuovo
            self.__coda  = nuovo
            nuovo.next   = nuovo
        else:
            nuovo.next       = self.__testa
            self.__coda.next = nuovo
            self.__testa     = nuovo
        self.__size += 1

    def insertLast(self, valore):
        nuovo = NodoC(valore)
        if self.isEmpty():
            self.__testa = nuovo
            self.__coda  = nuovo
            nuovo.next   = nuovo
        else:
            nuovo.next       = self.__testa
            self.__coda.next = nuovo
            self.__coda      = nuovo
        self.__size += 1

    def insertAfter(self, valore_riferimento, nuovo_valore):
        if self.isEmpty():
            raise IndexError("lista vuota")
        corrente = self.__testa
        while True:
            if corrente.valore == valore_riferimento:
                if corrente == self.__coda:
                    self.insertLast(nuovo_valore)
                    return
                nuovo         = NodoC(nuovo_valore)
                nuovo.next    = corrente.next
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next
            if corrente == self.__testa:
                break
        raise ValueError(f"{valore_riferimento} non trovato nella lista")

    def insertBefore(self, valore_riferimento, nuovo_valore):
        if self.isEmpty():
            raise IndexError("lista vuota")
        if self.__testa.valore == valore_riferimento:
            self.insertFirst(nuovo_valore)
            return
        corrente = self.__testa
        while corrente.next != self.__testa:
            if corrente.next.valore == valore_riferimento:
                nuovo         = NodoC(nuovo_valore)
                nuovo.next    = corrente.next
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next
        raise ValueError(f"{valore_riferimento} non trovato nella lista")

    def removeFirst(self):
        if self.isEmpty():
            raise IndexError("removeFirst da una lista vuota")
        valore = self.__testa.valore
        if self.__testa == self.__coda:
            self.__testa = None
            self.__coda  = None
        else:
            self.__testa     = self.__testa.next
            self.__coda.next = self.__testa
        self.__size -= 1
        return valore

    def removeLast(self):
        if self.isEmpty():
            raise IndexError("removeLast da una lista vuota")
        valore = self.__coda.valore
        if self.__testa == self.__coda:
            self.__testa = None
            self.__coda  = None
        else:
            corrente = self.__testa
            while corrente.next != self.__coda:
                corrente = corrente.next
            corrente.next = self.__testa
            self.__coda   = corrente
        self.__size -= 1
        return valore

    def remove(self, valore):
        if self.isEmpty():
            raise IndexError("lista vuota")
        if self.__testa.valore == valore:   # caso speciale: è la testa
            self.removeFirst()
            return
        if self.__coda.valore == valore:    # caso speciale: è la coda
            self.removeLast()
            return
        corrente = self.__testa
        while corrente.next != self.__testa:
            if corrente.next.valore == valore:
                corrente.next = corrente.next.next
                self.__size -= 1
                return
            corrente = corrente.next
        raise ValueError(f"{valore} non trovato nella lista")

    def traverse(self, passi):
        if self.isEmpty():
            raise IndexError("lista vuota")
        corrente = self.__testa
        for i in range(passi):
            print(f"passo {i + 1}: {corrente.valore}")
            corrente = corrente.next

    def peekFirst(self):
        if self.isEmpty():
            raise IndexError("lista vuota")
        return self.__testa.valore

    def peekLast(self):
        if self.isEmpty():
            raise IndexError("lista vuota")
        return self.__coda.valore

    def isEmpty(self):
        return self.__testa is None

    def size(self):
        return self.__size

    def __repr__(self):
        if self.isEmpty():
            return "CircularLinkedList([])"
        elementi = []
        corrente = self.__testa
        while True:
            elementi.append(str(corrente.valore))
            corrente = corrente.next
            if corrente == self.__testa:
                break
        return "CircularLinkedList([" + " → ".join(elementi) + " → ...])"

# BST (Binary Search Tree)
class NodoBST:
    def __init__(self, valore):
        self.valore = valore
        self.left   = None   
        self.right  = None  

class BST:
    def __init__(self):
        self.__radice = None

    def insert(self, valore):
        if self.__radice is None:
            self.__radice = NodoBST(valore)
        else:
            self.__insertRicorsivo(self.__radice, valore)


    def __insertRicorsivo(self, nodo, valore):
        if valore < nodo.valore:
            if nodo.left is None:
                nodo.left = NodoBST(valore)
            else:
                self.__insertRicorsivo(nodo.left, valore)
        else:
            if nodo.right is None:
                nodo.right = NodoBST(valore)
            else:
                self.__insertRicorsivo(nodo.right, valore)

    def search(self, valore):
        return self.__searchRicorsivo(self.__radice, valore)

    def __searchRicorsivo(self, nodo, valore):
        if nodo is None:
            return False
        if nodo.valore == valore:
            return True
        if valore < nodo.valore:
            return self.__searchRicorsivo(nodo.left, valore)
        else:
            return self.__searchRicorsivo(nodo.right, valore)

    def inOrder(self):
        elementi = []
        self.__inOrderRicorsivo(self.__radice, elementi)
        return elementi

    def __inOrderRicorsivo(self, nodo, elementi):
        if nodo is None:
            return
        self.__inOrderRicorsivo(nodo.left, elementi)
        elementi.append(nodo.valore)
        self.__inOrderRicorsivo(nodo.right, elementi)

    def isEmpty(self):
        return self.__radice is None

    def __repr__(self):
        return f"BST(inOrder={self.inOrder()})"
