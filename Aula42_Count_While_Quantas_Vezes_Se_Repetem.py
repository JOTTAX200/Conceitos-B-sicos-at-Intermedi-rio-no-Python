frase = 'o Python é uma linguagem de programação' \
    'Multiparadigma ' \
    'Python foi criado por Guido Van '

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_apareceu_atual = frase.count(letra_atual)
    i += 1

    if letra_atual == ' ':
        i += 1
        continue 

        
    if qtd_apareceu_mais_vezes <= quantas_vezes_apareceu_atual:
        qtd_apareceu_mais_vezes = quantas_vezes_apareceu_atual
        letra_apareceu_mais_vezes = letra_atual

print(f'A palavra que mais repete é "{letra_apareceu_mais_vezes}" e repete {quantas_vezes_apareceu_atual}')

