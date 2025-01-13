class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Au Au Au")

    def acordado(self):
        self.acordado = False
        print("zzzZZzzzZZzz")

cao_1 = Cachorro("Leão","Amarelo",False)
cao_2 = Cachorro("Jão", "Preto")

cao_1.latir()
print(cao_2.acordado())
