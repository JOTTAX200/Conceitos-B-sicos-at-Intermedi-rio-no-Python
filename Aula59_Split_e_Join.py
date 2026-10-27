"""
split e join com list e str
split - divide uma string (list)
join - une uma string
strip - 
"""

frase = '         Olha só       ,       que coisa interessante!        '
lista_frase_cruas = frase.split(',')


lista_frases = []
for i, frase in enumerate(lista_frase_cruas):
    lista_frases.append(lista_frase_cruas[i].strip())
  

print(lista_frase_cruas)
print(lista_frases)

# JOIN

#frases_unidas = '-'.join(lista_frases)
#print(frases_unidas)

