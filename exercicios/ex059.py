n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

escolha = 0
while escolha != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    escolha = int(input('Qual opção? '))
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} é {soma}')

    elif escolha == 2:
        mult = n1 * n2
        print(f'A multiplicação de {n1} x {n2} é {mult}')

    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')

    elif escolha == 4:
        print('Informe os numeros de novo:')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))

    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção invalida! Tente novamente')
print('Fim, até mais!')