"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

def soma(x ,y, z=None):
    if z is not None:
        print(f'x={x} y={y} z={z}' '|' 'x + y =', x + y +z)
    else:
        print(f'x={x} y={y}' '|' 'x + y =', x + y)    

soma(1,2)
soma(2, 4, 7) 



