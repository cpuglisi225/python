class Libro:
    def __init__(self, titolo, pagine, prezzo):
        self.titolo = titolo      # Attributo Pubbblico 
        self._prezzo = prezzo     # Attributo Protetto 
        self.__pagine = pagine    # Attributo Privato

    # Metodo per leggere l'attributo privato
    def get_pagine(self):
        return self.__pagine

    # Metodo per modificare l'attributo privato
    def set_pagine(self, nuove_pagine):
        if nuove_pagine > 0:
            self.__pagine = nuove_pagine


# Creazione di un oggetto
libro1 = Libro("Il Piccolo Principe", 96, 10.5)

# Accesso Attributo Pubblico
print(libro1.titolo)

# Accesso Attributo Protetto
print(libro1._prezzo)

# Accesso Attributo Privato
print(libro1.get_pagine())

# Modifica Attributo Privato
libro1.set_pagine(120)
print(libro1.get_pagine())