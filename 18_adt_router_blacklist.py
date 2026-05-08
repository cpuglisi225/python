'''Simula un sistema di controllo accessi integrato in un router. Per ogni pacchetto in arrivo il router deve decidere in tempo reale 
se l'IP sorgente è nella blacklist e bloccarlo.
Gli IP sono nella forma 192.168.1.1 - prima di inserirli nel BST vanno convertiti in interi usando la libreria ipaddress. 
Il BST lavora con interi, ma all'utente mostriamo sempre la forma leggibile.
1) Scrivi due funzioni di conversione - ipToInt(ip) e intToIp(n) - usando ipaddress.ip_address()
2) Genera 1000 IP casuali per la blacklist usando una list comprehension, convertili in interi e inseriscili nel BST
3) Genera 20 pacchetti in arrivo - 10 IP presi dalla blacklist e 10 IP nuovi mai visti - mescolali casualmente e inseriscili nella Queue
4) Processa i pacchetti dalla Queue uno per uno - per ognuno cerca l'IP nel BST e stampa BLOCCATO o PERMESSO
5) Stampa il riepilogo finale - quanti pacchetti bloccati e quanti permessi
6) Misura e confronta il tempo di ricerca nel BST e in una lista Python con gli stessi 1000 IP - stampa quante volte una struttura è più veloce dell'altra.
Considerare il pacchetto così formato:
pacchetto = {
    "ip_sorgente":      "192.168.1.1",
    "ip_destinazione":  "10.0.0.1",
    "porta_sorgente":   54321,
    "porta_destinazione": 80,
    "protocollo":       "TCP",
    "dimensione":       1500        # byte
}
'''
from adt import Queue, BST

from random import randint, shuffle

from ipaddress import ip_address

from time import perf_counter

def ip_to_int(ip):
    return int(ip_address(ip))

def int_to_ip(n):
    return str(ip_address(n))


def random_ip():
    return '.'.join([str(randint(0,254)) for _ in range(4)])

def pacchetto_random(ip_sorg):
    pacchetto = {
        "ip_sorgente":      ip_sorg,
        "ip_destinazione":  "10.0.0.1",
        "porta_sorgente":   54321,
        "porta_destinazione": 80,
        "protocollo":       "TCP",
        "dimensione":       1500        
    }
    return pacchetto

# Generazione di una blacklist di IP
ip_blacklist = []
for _ in range (1000):
    ip_blacklist.append(random_ip())

# Inserimento degli ip della blacklist in BST come int
blacklist_tree = BST()
for ip in ip_blacklist:
    blacklist_tree.insert(ip_to_int(ip))

# Generazione della coda di pacchetti con 10 IP blacklisted e 10 random
queue_pacchetti = Queue()
lista_ip = []

# IP casuali dalla blacklist
for _ in range (10):
    i = randint(0,len(ip_blacklist)-1)
    lista_ip.append(ip_blacklist[i])

# IP random
for _ in range (10):
    lista_ip.append(random_ip())

# Cambio casuale della posizione degli ip e inserimento in queue come pacchetti
shuffle(lista_ip)
for ip in lista_ip:
    queue_pacchetti.enqueue(pacchetto_random(ip))

# Analisi degli IP sorgente dei pacchetti
print('=' * 40)
print('      ANALISI PACCHETTI RICEVUTI')
print('=' * 40)
print(f'   {"IP SORGENTE":<18} {"ESITO"}')
pacchetti_bloccati = 0
pacchetti_permessi = 0
tot_pacchetti = queue_pacchetti.size()

while not queue_pacchetti.isEmpty():
    ip_sorgente = queue_pacchetti.dequeue()['ip_sorgente']
    int_ip_sorgente = ip_to_int(ip_sorgente)
    in_blacklist_tree = blacklist_tree.search(int_ip_sorgente)
    if in_blacklist_tree:
        pacchetti_bloccati +=1
        print(f'- {ip_sorgente:<18} BLOCCATO')
    else:
        pacchetti_permessi +=1
        print(f'- {ip_sorgente:<18} PERMESSO')

# Stampa dei risultati
print('-'*40)
print(f'Pacchetti analizzati:\t{tot_pacchetti}')
print(f'Pacchetti permessi:\t{pacchetti_permessi}')
print(f'Pacchetti bloccati:\t{pacchetti_bloccati}')
print('='*40)


# Conversione IP ad interi per escludere i tempi di conversione dalla misurazione
int_blacklist = [ip_to_int(ip) for ip in ip_blacklist]
int_lista_ip = [ip_to_int(ip) for ip in lista_ip]

# Confronto tempi ricerca in lista python e in BST
start = perf_counter()
for ip in int_lista_ip:
    if ip in ip_blacklist:
        pass
end = perf_counter()
tempo_lista = end - start

start = perf_counter()
for ip in int_lista_ip:
    blacklist_tree.search(ip)
end = perf_counter()
tempo_bst = end - start

print(f'Tempo ricerca in lista (s): {tempo_lista:.6f}')
print(f'Tempo ricerca in BST (s):   {tempo_bst:.6f}')

# Calcolo quante volte il BST è più veloce 
volte = tempo_lista / tempo_bst if tempo_bst > 0 else float('inf')
print(f'BST più veloce della lista: {volte:.2f} volte')
print('-'*40)