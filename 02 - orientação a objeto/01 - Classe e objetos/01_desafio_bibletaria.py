class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    def buzinar(self):
        print("Piiiiii")

    def parar(self):
        print("Parando bicicleta")
        print("Bicicleta parada")

    def correr(self):
        print("Vrummmmm")


b1 = Bicicleta("vermelha", "caloi", 2022, 650)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor,b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Vermelho", "Caloi", 2000, 120)
b2.buzinar()
print(b2.cor)