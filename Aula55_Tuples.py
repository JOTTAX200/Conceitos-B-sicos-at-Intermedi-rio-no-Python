"""
Tipo tupla - Uma lista imutável
"""

nomes = 'Marco', 'João', 'Fernanda'
print(nomes)


#CONVERSÃO DE TUPLE PARA LIST OU LIST PARA TUPLE


nomes = ['Marco', 'João', 'Fernanda']
nomes = tuple(nomes)
nomes = list(nomes)
print(nomes)