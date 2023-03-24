from random import randint
computador = randint(0,5)
usuario = int(input('Adivinhe o numero que o computador pensou: '))
if usuario == computador:
    print('Parabens, vooce conseguiu acertar')
else:
    print(f'Looser, o computador pensou no número {computador} nao no {usuario} ')