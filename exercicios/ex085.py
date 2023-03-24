numeros = [[], []]
valores = 0
for c in range (1, 7):
    valores = int(input(f'Digite o {c}º numero: '))
    if valores % 2 == 0:
        numeros[0].append(valores)
    else:
        numeros[1].append(valores)
print('-=' * 30)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares foram: {numeros[0]}')
print(f'Os valores impares foram: {numeros[1]}')

