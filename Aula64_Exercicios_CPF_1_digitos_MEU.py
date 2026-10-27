"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf_enviado_pelo_usario = "54589548828"

nove_digitos = cpf_enviado_pelo_usario[:9]

resultado = 0
contador_1 = 10

for digito in nove_digitos:
    resultado += int(digito) * contador_1
    contador_1 -= 1

digito_1 = resultado *10 % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

cpf_calculado = cpf_enviado_pelo_usario[:10]

dez_digitos = nove_digitos + str(digito_1)

resultado2 = 0
contador2 = 11

for digito_2 in dez_digitos:
    resultado2 += int(digito_2) * contador2
    contador2 -= 1
    
digito2 = resultado2 * 10 % 11
digito2 = digito2 if digito2 <= 10 else 0

cpf_calculado = f'{nove_digitos}{digito_1}{digito2}'

if cpf_enviado_pelo_usario == cpf_calculado:
    print(f'{cpf_calculado} é valido')

else:
    print('Cpf invalidado')    
