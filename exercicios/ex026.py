frase = str(input('Digite uma frase: ')).upper()
print(f'A letra A aparece {frase.count("A")} vezes na frase')
print(f'A primeira letra A aparece na posição {frase.find("A")+1} ')
print(f'A ultima vez que apareceu foi na posiçao {frase.rfind("A")+1}')