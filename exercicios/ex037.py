n = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
escolha = int(input('Sua escolha foi: '))

if escolha == 1:
    print(f'{n} convertido para BINÁRIO é igual {bin(n)[2:]}')
elif escolha == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}')
elif escolha == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
    print('Opção INALIDA!')