while True:
    n = int(input('Tabuada de qual valor? '))
    print('=' * 30)
    if n < 0:
        break
    for c in range(1 , 11):
        print(f'{n} x {c} = {n*c}')
    print('=' * 30)
print('Tchau, até a proxima!')