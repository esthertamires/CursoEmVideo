n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('Infelizmente você foi reprovado.')
elif 7 > media >= 6.9:
    print('Recuperação')
elif media >= 7.0:
    print('Aprovado')