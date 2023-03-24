palav = ('Justiça', 'Apavoro' ,'Costumes', 'Vingança',
         'Abraço', 'Perdao', 'Felicidade', 'Esperança',
         'Conjunto', 'Composto', 'Quadrado', 'Circulo')
for p in palav:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')