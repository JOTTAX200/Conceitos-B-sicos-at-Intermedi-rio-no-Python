""" Calculadora Exercicio"""

while True:
    numero_1 = input('Digite um número: ')
    numero_1 = float(numero_1)
    numero_2 = input('Digite outro número: ')
    numero_2 = float(numero_2)
    operacao = input('Qual operador? +, -, * ou /: ')
    
    if operacao == '+':
        print(f'{numero_1} + {numero_2} = ',numero_1 + numero_2)

    elif operacao == '-':
         print(f'{numero_1} - {numero_2} = ',numero_1 - numero_2)

    elif operacao == '*':
        print(f'{numero_1} * {numero_2} = ',numero_1 * numero_2)

    elif operacao =='/':
        print(f'{numero_1} / {numero_2} = ',numero_1 / numero_2)

    else:
        print('Operador Incorreto')
        continue

    sair =  input('Deseja sair? [s]im e [n]ão: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break
