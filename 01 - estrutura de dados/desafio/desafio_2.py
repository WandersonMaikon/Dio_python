# TODO: Crie uma função 'elementos_comuns' que receba duas listas de números inteiros:
def elementos_comuns(lista1, lista2):
    # Converte as listas de strings para conjuntos de inteiros
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))
    # Retorna a interseção dos dois conjuntos como uma lista
    return list(set1.intersection(set2))

# Divide as entradas em listas de strings
lista1 = input().split()
lista2 = input().split()

# Verifica se todos os elementos das listas podem ser convertidos para inteiros
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    # Chama a função para encontrar os elementos comuns
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")
