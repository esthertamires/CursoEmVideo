km = float(input('Qual a distancia da sua viagem em KM: '))

if km >= 200:
    print(f'O valor da sua passagem ficara em R${km*0.50}')
else:
    print(f'O valor da sua passagem ficará em R${km*0.45}')