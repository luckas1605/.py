import os

lista = []


while True:
    print("Selecione uma opção: ")
    opcao = input("[i]nserir [a]pagar [l]istar [f]inalizar: ")

    if opcao == 'i':
        os.system('cls')
        valor = input('Digite um produto: ')
        lista.append(valor)

    elif opcao == 'a':
        indice_str = input(
            'Escolha um indice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possivel apagar este indice. ')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)
    elif opcao == 'f':
        break
    
    else:
         os.system('cls')
         print("Por favor digite 'i', 'a', 'l' ou 'f'")

