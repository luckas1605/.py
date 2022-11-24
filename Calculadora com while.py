
while True:
    
    nmr1 = input("digite um numero: ")
    operador = input("digite um operador (+ - / *): ")
    nmr2 = input("digite outro numero: ")
        
    numeros_validos = None
    try:
        num_1_float = float(nmr1)
        num_2_float = float(nmr2)
        numeros_validos = True
    except:
        numeros_validos = None
    if numeros_validos is None:
        print("Um ou ambos numeros digitados são invalidos.")
        continue

    operadores_permitidos = "+-/*"

    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue
    if operador not in operadores_permitidos:
        print("Operador invalido.")
        continue 
    
    if operador == '+':
        print(f"{nmr1} + {nmr2} = ", float(nmr1) + float(nmr2))  
    elif operador == '-':
        print(f"{nmr1} - {nmr2} = ", float(nmr1) - float(nmr2))
    elif operador == '/':
        print(f"{nmr1} / {nmr2} = ", float(nmr1) / float(nmr2))
    else:
        operador == '*'
        print(f"{nmr1} * {nmr2} = ", float(nmr1) * float(nmr2))

    
        
    sair = input("Para encerrar digite: [s], e para continuar digite qualquer coisa: ").lower().startswith('s')
    if sair is True:
        break
