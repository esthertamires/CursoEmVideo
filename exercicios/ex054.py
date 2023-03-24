from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1 , 8):
    nascimento = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = atual - nascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todos tivemos {totmaior} pessoas maiores de idade')
print(f'E tambem tivemmos {totmenor} pessoas menores de idade')
