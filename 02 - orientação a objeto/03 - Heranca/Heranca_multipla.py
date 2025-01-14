class Animal:
    def __init__(self, n_patas):
        self.n_patas = n_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.
        join([f'{chave}={valor}' for chave, valor in 
        self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, n_patas, cor_pelo):
        self.cor_pelo = cor_pelo
        super().__init__(n_patas)


class Ave(Animal):
    def __init__(self, n_patas):
        super().__init__(n_patas)

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

gato = Gato(4, "Braco")
print(gato)