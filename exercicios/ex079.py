numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado, nao será adicionado')
    r = str(input('Quer continuar [S/N]: '))
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Os valores digitados foram {numeros}')