nome = "Wanderson"
idade = 18
profissao = "programador"
linguagem = "Python"

dados = {"nome": "maikon", "idade":31}

print("Nome: %s idade : %d " % (nome,idade))
print("Nome: {} idade: {}".format(nome,idade))
print("Nome: {name} idade: {age}".format(age = idade, name = nome))
print("Nome: {nome} idade: {idade}".format(**dados))
print(f"nome: {nome} idade: {idade}")