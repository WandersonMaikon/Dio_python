class Animal:
    def __init__(self, n_patas):
        self.n_patas = n_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.
        join([f'{chave}={valor}' for chave, valor in 
        self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **km):
        self.cor_pelo = cor_pelo
        super().__init__(**km)


class Ave(Animal):
    def __init__(self, cor_bico ,**km):
        self.cor_bico = cor_bico
        super().__init__(**km)

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

gato = Gato(n_patas=4,cor_pelo="Branco")
print(gato)

pato = Ave(n_patas=2, cor_bico="Amarelo")
print(pato)