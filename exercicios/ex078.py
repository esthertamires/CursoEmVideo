list = list()
for cont in range(0, 5):
    list.append(int(input(f'Digite um valor pra posição {cont}: ')))
print(f'A lista digitada foi {list}')
print(f'O maior numero representado na lista foi {max(list)} e sua posição é a {list.index(max(list))}')
print(f'o menor numero representado na lista foi {min(list)} e sua posição é a {list.index(min(list))}')