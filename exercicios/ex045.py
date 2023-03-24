from random import randint
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual vai ser a sua jogada: '))
print(f'O computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')

# PEDRA
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('OPÇÃO INVALIDA')
# PAPEL
elif computador == 1:

    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
#TESOURA
elif computador == 2:

    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')