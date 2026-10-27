"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'joao'  # iterável
iteratador = iter(texto)

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except InterruptedError:
        break   
"""

for letra in texto:
    print(letra)
    """