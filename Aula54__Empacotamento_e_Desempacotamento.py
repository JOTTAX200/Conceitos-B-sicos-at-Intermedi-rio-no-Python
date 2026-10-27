"""
Introdução ao empacotamento e desempacotamento
"""

nome1, *resto = ['Marco', 'João', 'Fernanda']
print(nome1)

#OU

nome2, *resto = ['Marco', 'Joao', 'Fernanda']
print(nome2)

#OU

nome3, *_ = ['Marco', 'Joao', 'Fernanda']
print(nome3)

""""""
#SE EU QUISER PEGAR OUTROS ITEMS DA LISTA

_, nome4, _, *_ = ['Marco', 'Joao', 'Fernanda']
print(nome4)

