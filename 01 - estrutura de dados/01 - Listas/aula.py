# Lista
frutas = ["maça", "laranja", "uva"]
print(frutas[0])
print(frutas[-1])

# matriz
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
print(matriz[1][2])
print(matriz[0][2])
print(matriz[2][2])

# Fatiamento

lista = ["P", "Y", "T", "H", "O", "N"]
print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[::])
print(lista[::-1])

# Percorrer lista
carros = ["uno", "celta", "palio"]
for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Modificando valores
numeros = [1, 30, 21, 2, 8, 54, 32]
pares = []
for numero in numeros:
    if (numero % 2 == 0):
        pares.append(numero)
        print(pares[::])
# Outra versão
numeros = [1, 30, 21, 2, 8, 54, 32]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares[::])

# Ao quadrado
numero = [1, 30, 21, 2, 8, 54, 32]
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado[::])

# Outra versão
numero = [1, 30, 21, 2, 8, 54, 32]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado[::])