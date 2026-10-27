"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['joao', 'higor']
lista_b = lista_a.copy()

lista_a[0] = 'bosta seca'
print(lista_a)
print(lista_b)


texto = 'joao'
texto_1 = texto
texto = 'pedro'
print(texto_1, texto)