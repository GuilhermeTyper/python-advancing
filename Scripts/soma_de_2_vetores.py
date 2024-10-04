i = 0
v1 = 10 * [0]
v2 = 10 * [0]
v3 = 10 * [0]

while i < 10:
    num1 = int(input(f'Digite o {i} da lista 1: '))
    v1[i] = num1
    num2 = int(input(f'Digite o {i} da lista 2: '))
    v2[i] = num2
    v3[i] = num1 + num2
    i = i + 1
print(f'A soma de cada indice dos vetores é: {v3}')

