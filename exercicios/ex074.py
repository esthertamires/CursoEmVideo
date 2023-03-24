from random import randint
numeros = (randint(1,10), randint(1,10),randint(1,10)
           ,randint(1,10), randint(1,10))
print('Os numeros sorteados foram:', end=' ')
for n in numeros:
    print(f'{n} ', end='')
print(f'''
O maior numero da lista foi {max(numeros)}''')
print(f'o menor numero da lista foi {min(numeros)}')