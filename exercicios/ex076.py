lista = ('Mouse', 120,
         'Teclado', 200,
         'Mouse pad', 70,
         'Monitor 1', 400,
         'Monitor 2', 350,
         'Caixa de som', 50,
         'Headset', 160,
         'Nobreak', 600,
         'Filtro de linha', 25,)
print('-' * 40)
print(f'{"PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:7.2f}')