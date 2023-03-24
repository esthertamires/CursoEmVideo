nome = str(input('Qual é o seu nome? '))
if nome == 'Esther':
    print('que nome bonito!')
elif nome == 'Douglas' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bbem popular no Brasil.')
elif nome in 'Ana Claúdia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('seu nome é bem normal.')
print(f'Tenho um bom dia {nome}')