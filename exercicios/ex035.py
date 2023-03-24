a = float(input('Lado a: '))
b = float(input('Lado b: '))
c = float(input('Lado c: '))

if (b-c) < a < b + c and (a-c) < b < a + c and (a-b) < c < a + b:
    print('A reta consegue formar um TRIANGULO')
    if a == b == c:
        print('Equilátero')
    elif a != b != c != a:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Sem triangulos pra você bro')