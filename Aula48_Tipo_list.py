"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
#print(bool(lista))# Falsy
#print(lista, type(lista))#

#É possivel criar uma lista dentro de uma lista usando "[]"

#Possui Índices
#.........0.....1..........2..........3...4...
#.........-5.....-4......-3..........-2..-1...
lista = [1235, 1.2, 'João Gabriel', True, [] ]
lista[-3] = 'Fernanda'
print(lista[-3])
print(lista[-3], type(lista[-3]))

