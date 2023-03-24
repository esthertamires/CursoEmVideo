a = float(input('Lado a: '))
b = float(input('Lado b: '))
c = float(input('Lado c: '))

if a < b + c and b < a + c and c < a + b:
    print('A reta consegue formar um TRIANGULO')
    if a == b == c:
        print('EQUILÁTERO!')
    if a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('Sem triangulos pra você bro')