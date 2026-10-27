entrada = input('[E]ntrar e [S]air: ')
senha_digitada = input('insira a senha: ')

senha_permitida = '123456'
if entrada == 'E' or 'e' and senha_digitada == senha_permitida:
    print('Entrou')
else:
    print('Saiu')    