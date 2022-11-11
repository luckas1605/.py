nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")


if nome and idade:

    print(f"O seu nome é {nome} ")
    print(f'O seu nome invertido fica é {nome[::-1]}')

    if " " in nome:
        print("Seu nome contem espaços")
    else:
        print("Seu nome nao contem espaços")

    quantidade = len(nome)
    print("O seu nome tem {} letras".format(quantidade))

    print(f"A primeiro letra do seu nome é {nome[0]} ") 
    print(f"A ultima letra do seu nome é {nome[-1]} ")
else:
    print("Desculpe vc deixou campos vazios")
