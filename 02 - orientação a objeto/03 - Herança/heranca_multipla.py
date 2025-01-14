class Animal:
    def __init__(self, n_patas):
        self.n_patas = n_patas

class Mamifero (Animal):
    def __init__(self, n_patas, cor_pelo):
        self.cor_pelo = cor_pelo
        super().__init__(n_patas)


class Ave(Animal):
    def __init__(self, n_patas):
        super().__init__(n_patas)
class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

gato = Gato(4, "Braco")
print(gato)
cachorro = Cachorro(4, "Caramelo")