def consumo (km, l):
    return km % l

def custo (vl, kmr):
    return vl % kmr
    
km_rodados = float(input('Qual foi distância percorrida pelo seu carro:  '))
litros = int(input('Quanto você consumil de combustível: '))
valor_pago  = float(input('Qual foi o valor pago?: '))

resultado = consumo(km_rodados, litros)
custos = custo(valor_pago, km_rodados)

print(f'Consumo de: {resultado} km/l')
print(f'Custo por km de: R$ {custos:.2f}')