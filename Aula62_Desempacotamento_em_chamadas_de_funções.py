# Desempacotamento em chamadas 
# de métodos e funções

string = 'ABCD'
lista = ['Maria','Helena',1, 2 , 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

a, b,*_ , c  = lista
print(a,c)
print(*lista)

#print(*string)
#print(*tupla)

#EXEMPLO: SE VOCÊ QUISER FAZER NUMA LISTA MAIS COMPLEXA, VOCE FAZ ISSO:
 
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', (10, 20, 30, 40, 50)],  # 2
]

print(*salas, sep='\n')