class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        self.aperto = False  # stato del libro

    def apri(self):
        if not self.aperto:
            self.aperto = True
            print(f"Hai aperto il libro '{self.titolo}'.")
        else:
            print("Il libro è già aperto.")

    def chiudi(self):
        if self.aperto:
            self.aperto = False
            print(f"Hai chiuso il libro '{self.titolo}'.")
        else:
            print("Il libro è già chiuso.")

    def leggi(self):
        if self.aperto:
            print(f"Stai leggendo '{self.titolo}' di {self.autore}.")
        else:
            print("Apri il libro prima di leggere.")


# Creazione di un oggetto (istanza)
libro1 = Libro("Il Piccolo Principe", "Antoine de Saint-Exupéry", 96)

# Uso dei metodi
libro1.leggi()
libro1.apri()
libro1.leggi()
libro1.chiudi()