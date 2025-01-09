def verificador_ano_bissexto():
    ano = int(input("Digite o ano: "))  # Solicita ao usuário para inserir o ano
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("SIM")
    else:
        print("NÃO")

verificador_ano_bissexto()


# TODO: Verifique se o ano é bissexto utilizando uma estrutura de controle condicional, como if/else:

