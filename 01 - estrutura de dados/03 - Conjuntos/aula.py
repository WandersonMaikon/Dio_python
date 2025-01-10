# Eliminar registro duplicados
# Não garante a ordem
print(set([1,2,3,3,4,2]))
set('abacaxi')
set(("palio", "gol","celta","palio"))

numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])

#exemplo percorrendo conjunto

carros = {"palio","gol","celta"}

for carro in carros:
    print(carro)

# é possível unir os conjuntos
conjunto_a = {1, 2}
conjunto_b = {3, 4}

uniu = conjunto_a.union(conjunto_b)
print(uniu)

# intersecção é usado para pegar apenas o que é igual

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
inter = conjunto_a.intersection(conjunto_b)
print(inter)

# também é possível pegar apenas o que é diferente
# ou existe somente neste conjunto

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
difer = conjunto_a.difference(conjunto_b)
print(difer)

