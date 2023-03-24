from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} em {atual}')
if idade == 18:
    print('Está na hora de você se alistar!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não tem 18. Falta {saldo} anos para o alistamento')
elif idade > 18:
    saldo = idade - 18
    print(f'Você ja deveria ter se alistado há {saldo} ano/s')