from abc import ABC, abstractmethod

# Classe Astratta
class Libro(ABC):
    
    @abstractmethod
    def descrizione(self):
        pass

# Classi Concrete
class LibroCartaceo(Libro):
    def descrizione(self):
        print("Sono un libro cartaceo")

class Ebook(Libro):
    def descrizione(self):
        print("Sono un ebook")

# istanziazione oggetti
libro1 = Libro()
libro2 = Ebook()

# lista di oggetti
lista_libri = [libro1, libro2]

# polimorfismo
for l in lista_libri:
    l.descrizione()