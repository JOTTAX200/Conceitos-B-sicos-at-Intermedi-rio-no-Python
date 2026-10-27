palavra_secreta = 'Tiquinho'
contagem = 1



Digite_uma_letra = input('Digite uma letra: ')


if len(Digite_uma_letra) > 1:
    print('Digite apenas uma letra')

else:
    Digite_uma_letra = input('Digite uma letra: ')

if Digite_uma_letra == palavra_secreta:
    print('Parabéns você acertou')
    print(contagem)


