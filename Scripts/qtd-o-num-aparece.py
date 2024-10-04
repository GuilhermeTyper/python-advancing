v = 5 * [0]
i = 0

def qtd_num(v,num):
    i = 0
    cont = 0 
    while i < 5:
        if v[i] == num:
            cont = cont + 1
        i = i + 1
    return cont

while i < 5:
    num = int(input(f'Digite o {i} número: '))
    v[i] = num
    i = i + 1

num = int(input("Digite qual o núemro deseja verificar: "))


tot = qtd_num(v,num)


print(f'o número: {num} aparece {tot} vezes')