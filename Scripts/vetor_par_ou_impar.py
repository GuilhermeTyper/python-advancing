v = 10 * [0]
i = 0
contpar = 0

while i < 10:
    num = int(input(f'Digite o {i} número: '))
    v[i] = num
    if v[i] % 2 == 0:
        contpar = contpar + 1
    i = i + 1
print(f'Foram encontrados: {contpar} números pares')