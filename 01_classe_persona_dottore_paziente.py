"""
Ereditarietà in Python:
- Classe base: Persona (nome, cognome, età)
- Sottoclassi:
  - Dottore (matricola, reparto, pazienti)
  - Paziente (codice_id, gruppo sanguigno, patologie, allergie)
Funzionalità:
- Stampa dati oggetti
- Gestione lista pazienti (aggiunta/visualizzazione)
02/04/26
"""
class Persona():

    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
    
class Dottore(Persona):

    def __init__(self, nome, cognome, matricola, eta, reparto, pazienti):
        Persona.__init__(self, nome, cognome, eta)
        self.reparto = reparto
        self.matricola = matricola  
        self.pazienti = pazienti

    def aggiungi_pazienti(self):
        paziente = input('Aggiungi paziente: ')
        self.pazienti.append(paziente)
        
    def mostra_pazienti(self):
        for paziente in self.pazienti:
            print(paziente)

    def __str__(self):
        return f'Dottore:\t{self.nome} {self.cognome}\nMatricola:\t{self.matricola}\nEtà:\t\t{self.eta}\nReparto:\t{self.reparto}'

class Paziente(Persona):

    def __init__(self, nome, cognome, codice_id, eta, gruppo_sanguigno, patologie, allergie):
        Persona.__init__(self, nome, cognome, eta)
        self.codice_id = codice_id
        self.gruppo_sanguigno = gruppo_sanguigno
        self.patologie = patologie
        self.allergie = allergie

    def __str__(self):
        return f'Paziente:\t{self.nome} {self.cognome}\nCod. Id.:\t{self.codice_id}\nEtà:\t\t{self.eta}\nGr. Sang.:\t{self.gruppo_sanguigno}\nPatologie:\t{self.patologie}\nAllergie:\t{self.allergie}'

d = Dottore('Mario', 'Rossi', 'M001', 20, 'Chirurgia', ['Luigi Bianchi', 'Maria Verdi', 'Alberto Gallo'])
p1 = Paziente('Luigi', 'Bianchi', '001', 32, 'A-', ['Diabete', 'Ipertensione'], ['Nessuna'])
p2 = Paziente('Maria', 'Verdi', '002', 66, 'B+', ['Insufficenza Renale'], ['Mandorle', 'Nocciole'])

print(d)
print('='*50)
print(p1)
print('-'*50)
print(p2)
print('='*50)
print(f'Lista assistiti Dott. {d.nome} {d.cognome}: ')
d.mostra_pazienti()
print('-'*50)
d.aggiungi_pazienti()
print('-'*50)
d.mostra_pazienti()