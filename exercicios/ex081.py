valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Voce digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os alores em ordem decrecente sao {valores}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista!')
else:
    print('o valor 5 nao faz parte da lista')