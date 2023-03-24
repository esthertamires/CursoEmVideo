resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]')).strip()[0].upper()
media = soma / quant
print(f'Você digitou {quant} numero e a media foi {media:.2f}')
print(f'o maior valor foi {maior} e o menor {menor}')
