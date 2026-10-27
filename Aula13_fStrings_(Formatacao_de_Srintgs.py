nome= 'João Gabriel'
altura = 1.73
peso = 64
imc = peso / (altura * altura)

linha_1 = f'Seu nome é {nome} {altura} de altura'
linha_2 = f'Pesa {peso} Quilos e seu IMC é de'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)