class Libro:
    def descrizione(self):
        print("Questo è un libro generico")


class LibroDigitale(Libro):
    def descrizione(self):
        print("Questo è un ebook")


# istanziazione oggetti
libro1 = Libro()
libro2 = LibroDigitale()

# lista di oggetti
lista_libri = [libro1, libro2]

# polimorfismo
for l in lista_libri:
    l.descrizione()