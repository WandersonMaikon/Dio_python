# Um dicionário é um conjunto não-ordenado de pares
# chave:valor, onde as chaves sao únicas em uma dada instância
# do dicionário. Dicionários são delimitados por chaves: {}, e
# contém uma lista de pares chave:valor separada por vírgulas.

# Exemplo
pessoa = {"nome": "Guilherme", "idade": 28}

pessoa = dict(nome="Guilherme", idade=28)

# {"nome": "Guilherme", "idade": 28,

pessoa["telefone"] = "3333-1234"  # "telefone": "3333-1234"}

print(pessoa)

# acesso aos dados


dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

dados["idade"] # 28

dados["nome"]  #"Guilherme"

dados["telefone"] # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}

# Dicionário alinhados
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

print(contatos["giovanna@gmail.com"]["telefone"])

# Iterar dados

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

# utilizando get
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos ["chave"] # KeyError

contatos.get("chave") # None
contatos.get("chave", {}) # {}
contatos.get("guilherme@gmail.com", {})