n = cont = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma = soma + n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print(f'Foi digtado {cont} numeros e a soma deles foi {soma}')