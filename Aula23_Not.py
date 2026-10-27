#Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

print(not True)
print(not False)

senha = input('Senha: ')
senha_eu = '1234'

if not senha:
    print('Você nao digitou nada')
elif senha == senha_eu:
    print('entrou hehe')
else:
    print('Senha totalmente incorreta')    
