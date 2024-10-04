import os

def criar_vetor():
    vetor = 10*[0]
    i = 1
    while i < 10:
        vetor[i] = int(input(f'Digite o {i}º número: '))
        os.system('cls')
        i = i + 1
    return vetor
user = criar_vetor()

i = 1
soma = 0
qtd = 0
while i < 10:
    if user[i] > 50:
        qtd = qtd +1
    soma = soma + user[i]
    i = i + 1
media = soma/10
print(f'A média de números positivos é: {media}')
print()
print(f'A quantidade de valores maiores que 50 é: {qtd}')
print()