# Superclasse
class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore


# Classe derivata (Sottoclasse)
class LibroBiblioteca(Libro):
    def __init__(self, titolo, autore, scaffale):
        super().__init__(titolo, autore)  # Eredita Attributi
        self.scaffale = scaffale          # Nuovo Attributo

    def info(self):
        print(f"{self.titolo} di {self.autore}, scaffale {self.scaffale}")


libro1 = LibroBiblioteca("Il Piccolo Principe", "Saint-Exupéry", "A3")
libro1.info()