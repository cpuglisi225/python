'''
1)Genera una lista di 1000 numeri casuali tra 1 e 10k usando una list comprehnsion
2)Inserisci gli stessi 1000 numeri sia nella lista linkata che nel BST
3)Scegli un numero da cercare - prendi il 500esimo elemento della lista generata
4)Misura il tempo di ricerca nella lista collegata usando time.perf_counter()
5)Misura il tempo di ricerca nel BST usando time.perf_counter()
6)Stampa i due tempi e calcola quante volte una struttura è più veloce dell'altra
'''
from random import randint
from time import perf_counter

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
        if self.__testa.valore == target:
            self.insertFirst(target)
            return
        corrente = self.__testa
        while corrente.next is not None:
            if corrente.next.valore == target:
                return
            else: 
                corrente = corrente.next
        return False

    def __repr__(self):
        elementi = []
        corrente = self.__testa
        while corrente is not None:
            elementi.append(str(corrente.valore))
            corrente = corrente.next
        return "LinkedList([" + " → ".join(elementi) + "])"
    


# Lista di 1000 numeri casuali in [1, 10 000]
numbers = [randint(1,10000) for _ in range(1000)]

# Creazione e popolamento di linked list e di BST
lnkd_lst = LinkedList()
binary_tree = BST()
for number in numbers:
    lnkd_lst.insertLast(number)
    binary_tree.insert(number)

# L'elemento da cercare è quello di posto 500 in numbers
target = numbers[500]
print('Target:','\t'*4, target)

# Ricerca in LINKED LIST e misura del tempo impiegato
print('Searching in Linked List: ', end='')
if not lnkd_lst.isEmpty():
    start = perf_counter()
    lnkd_lst.search(target)
    end = perf_counter()
    lnkdlst_search_time = end - start
    print('\t\tFound!')
else:
    print('No element in Linked List.')

# Ricerca in BST e misura del tempo impiegato
print('Searching in BST: ', end ='')
if not binary_tree.isEmpty():
    start= perf_counter()
    binary_tree.search(target)
    end  = perf_counter()
    bst_search_time = end - start
    print('\t\t\tFound!')
else: 
    print('No element in BST.')

# Risultati
print('-'*60)
print(f'Binary Tree Searching Time(s):\t\t{bst_search_time:.6f}')
print(f'Linked List Searching Time(s):\t\t{lnkdlst_search_time:.6f}')
print('='*60)
percentage = ((lnkdlst_search_time - bst_search_time)/lnkdlst_search_time)*100
print(f'Searching in BST is {(percentage):.2f}% faster than in a Linked List.')
