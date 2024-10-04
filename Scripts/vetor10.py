import os

def criar_vetor():
    vetor = 10*[0]
    i = 0
    while i < 10:
        vetor[i] = int(input(f'Digite o {i}º número: '))
        os.system('cls')
        i = i + 1
    return vetor

user = criar_vetor()
i = 0
soma = 0
maiorVal = 0
vetMaiorVal = 10*[0]
while i < 10:
    if  user[i] > maiorVal:
        maiorVal = user[i]
        vetMaiorVal[i] =  maiorVal
    soma = soma + user[i]
    i = i + 1
media = soma/10
i = 0
print(f'Os maiores números foram:')
while i < 10:
    if vetMaiorVal[i] > media:
        print(f'{vetMaiorVal[i]} e está na posição {i}')
    i = i +1
