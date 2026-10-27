"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
lista_compras = []

while True:
    print('Selecione a opção')
    opcoes = input('[i]nserir, [a]pagar, [l]istar: ')

    if opcoes == 'i':
        inserir = input('Valor: ')
        lista_compras.append(inserir)
        print(lista_compras)

    elif opcoes == 'l':
        for indice, nome in enumerate(lista_compras):
            print(indice, nome)    

    elif opcoes == 'a':
        delete = input('Escolha um Indice para apagar: ')
        delete = int(delete)
        del lista_compras[delete]
        print(lista_compras)   

    else:
        print('Errado, escolha a opção certa')    
          

    


        


    


