casa = float(input('Qual o valor da casa desejada? R$'))
salario = float(input('Seu salario R$'))
anos = int(input('Em quanto anos você deseja pagar? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Sua casa no valor de R${casa:.2f} em {anos} anos, a prestação vai ser de R${prestação:.2f}')
if prestação <= minimo:
    print('Emprestimo aprovado')
else:
    print('Emprestimo NEGADO,a parcela do emprestimo execeu 30% do seu salario ')


