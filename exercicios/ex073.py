times = ('Palmeiras','Internacional','Fluminense','Corinthians',
         'Flamengo', 'Athletico-PR', 'Atlético-MG','Fortaleza',
         'São Paulo', 'América-MG','Botafogo','Santos','Goiás',
         'Bragantino','Coritiba','Cuiabbá','Ceará SC','Alético-GO',
         'Avaí','Juventude')
print('--' * 15)
print(f'Lista de times do Brasileirão : {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 ultimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 15)
print(f'O botafogo está na {times.index("Botafogo")+1}ª posição')