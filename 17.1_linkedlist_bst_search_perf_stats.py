"""
Confronto statistico tra lista linkata e BST nella ricerca di elementi.

Genera n (100, 1 000, 10 000) numeri casuali tra 1 e 10.000, li inserisce in una lista linkata 
e in un BST, e misura il tempo di ricerca su 1000 ripetizioni del valore intermedio.
Calcola media, deviazione standard e rapporto di velocità tra le strutture per ogni n.
"""

from random import randint
from time import perf_counter
from statistics import mean, stdev

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
    
sizes = [100, 1000, 10000]
iterations = 1000 

results = {}

print("="*60)
print ('\t LINKED LIST vs BST SEARCH BENCHMARK\t')
print(f'\t\t{iterations} iterations\t')
print("="*60)

for n in sizes:
    times_list = []
    times_bst = []

    for i in range(iterations):

        # Lista di n numeri casuali in [1, 10 000]
        numbers = [randint(1,10000) for _ in range(n)]

        # Creazione e popolamento di linked list e di BST
        lnkd_lst = LinkedList()
        binary_tree = BST()
        for number in numbers:
            lnkd_lst.insertFirst(number)
            binary_tree.insert(number)

        # L'elemento da cercare è quello di posto n//2 in numbers
        target = numbers[n//2]

        # Ricerca in LINKED LIST e misura del tempo impiegato
        if not lnkd_lst.isEmpty():
            start = perf_counter()
            lnkd_lst.search(target)
            end = perf_counter()
            lst_search_time = end - start
            times_list.append(lst_search_time)
        else:
            print('No element in Linked List.')

        # Ricerca in BST e misura del tempo impiegato
        if not binary_tree.isEmpty():
            start= perf_counter()
            binary_tree.search(target)
            end  = perf_counter()
            bst_search_time = end - start
            times_bst.append(bst_search_time)
        else: 
            print('No element in BST.')
    
    # Calcolo media, dev. std per linked list e BST
    mean_list = mean(times_list)
    std_list = stdev(times_list)

    mean_bst = mean(times_bst)
    std_bst = stdev(times_bst)

    speedup = mean_list / mean_bst

    #Dizionario con risultati
    results[n] = {
        "list_mean": mean_list,
        "list_std": std_list,
        "bst_mean": mean_bst,
        "bst_std": std_bst,
        "speedup": speedup
    }

    # Risultati
    print(f"\nData structure size: {n} elements")    
    print("-"*60)
    print(f"{'ADT':<20}\t{'Mean Time (s)':>15}\t{'Std. Dev. (s)':>15}")
    print(f"{'Linked List':<20} {mean_list:>15.6f} {std_list:>15.6f}")
    print(f"{'BST':<20} {mean_bst:>15.6f} {std_bst:>15.6f}")
    print("-"*60)

    if speedup > 1:
        print(f"BST is faster than the list by {speedup:.2f}x")
    elif speedup < 1:
        print(f"List is faster than BST by {1/speedup:.2f}x")
    else:
        print("BST and list have similar performance")

    print("="*60)