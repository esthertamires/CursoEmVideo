salario = float(input('Informe o seu salario atual R$ '))
if salario > 1250.00:
    print(f'Seu salario receberá um aumento de 10% e ficará em {salario + (salario * 10/100):.2f}')
else:
    print(f'Seu salario de {salario} terá um aumento de 15% e será {salario + (salario * 15/100):.2f}')