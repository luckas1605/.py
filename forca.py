import os


palavra_secreta = input("Digite uma palavra: ")
letras_Acertadas = ''
numeros_de_tentativas = 0

while True:

    letra_digitada = input("Digite uma letra:")

    if numeros_de_tentativas >= 6:  
        print("Você perdeu!")
        break

    if len(letra_digitada) > 1: 
        print("Digite apenas uma letra.")
        continue

    if letra_digitada in palavra_secreta:
        letras_Acertadas += letra_digitada
    else:
        numeros_de_tentativas += 1
        print(f"Você errou tente novamente, {numeros_de_tentativas} tentativas de 6.")
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_Acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
        
    print(palavra_formada)
    
    if palavra_formada == palavra_secreta:
        print("Parabés você ganhou!!!")
        print("A palavra era:", palavra_formada)
        break
