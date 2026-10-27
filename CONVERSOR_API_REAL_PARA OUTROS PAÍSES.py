
while True:
    print('Escolha a moeda que você deseja converter com o Real')
    opcoes = input('Escolha a moeda: [E]uro, [D]olar, [L]ibra:  ')
    

    if opcoes == 'E' or 'e':
        valor = float(input('Insira o valor que deseja: '))
        print(valor * 0.15)

    elif opcoes == 'D' or 'd':
        valor = float(input('Insira o valor que deseja: '))
        print(valor * 0.17)

    elif opcoes == 'L' or 'l':
        valor = float(input('Insira o valor que deseja: '))
        print(valor * 0.13)

    else:
        print('Ops acho que digitou errado') 

    sair =  input('Deseja sair? [s]im e [n]ão: ').lower().startswith('s')

    if sair is True:
        break



        
        

