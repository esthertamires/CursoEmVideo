cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete','oito','nove',
        'dez','onze','doze','treze','quatorze','quinze',
        'dezesseis', 'dezessete', 'dezoito','dezenove',
        'vinte')
while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente de novo.')
print(f'voce digitou o numero {cont[n]}')