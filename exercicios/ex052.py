n = int(input('Digite um número : '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        total += 1
    else:
        print(f'{c}')
print(f'O número {n} foi divisivel {total} vezes')
if total == 2:
    print('E é por isso ele É PRIMO!')
else:
    print('é por isso que ele NÃO É PRIMO')
