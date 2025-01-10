# Adicionar um novo valor a lista
# append
lista = []
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)  # [1, "Python", [40, 30, 20]]

# Limpar os valores de uma lista
# clear
lista = [1, "Python", [40, 30, 20]]
print(lista)
lista.clear()
print(lista)

# Copiar os valores outra lista
#copy
lista = [1, "Python", [40, 30, 20]]
lista.copy()
print(lista)  # [1, "Python", [40, 30, 20]]

# Contar a posição do elemento em uma lista

cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelho")  # 1
cores.count("azul")  # 2
cores.count("verde")  # 1

lista = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(lista)