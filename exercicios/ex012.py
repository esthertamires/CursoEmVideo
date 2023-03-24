produto = float(input('Digite o preço do produto: R$ '))
print(f'O produto com o preço de R${produto:.2f} novo preço com 5% de desconto ficará em R${produto - (produto * 5/100):.2f}')