from random import randint
computador = randint(0,10)
acertou = False
tentativas = 0
while not acertou:
    usuario = int(input('Adivinhe o numero que o computador pensou entre 0 e 10: '))
    tentativas += 1
    if usuario == computador:
        acertou = True
    else:
        if usuario < computador:
            print('Maior..')
        elif usuario > computador:
            print('Menor..')
print(f'Parabens, voce conseguiu acertar, tentando {tentativas} vezes')
