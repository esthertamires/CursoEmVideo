velocidade = float(input('Qual é a velocidade do veiculo? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'Puts man, você foi multado sua multar vai ficar no valor de R${multa}')
else:
    print('Continue dirigindo com segurança filha da puta')