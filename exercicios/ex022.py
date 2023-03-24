nome = str(input('Digite seu nome completo: ')).strip()
print(f"""O nome com todas as letras maiúsculas: {nome.upper()}
O nome com todas as letras minúsculas: {nome.lower()}
Total de letras que o nome tem {(len(nome) - nome.count(' '))}
Seu primeiro nome tem {nome.find(' ')} letras""")

