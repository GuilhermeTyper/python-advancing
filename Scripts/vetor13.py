import os
meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
i = 0
soma = 0
temperatura = 11*[0]
acima_media = 0
while i < 11:
    temperatura[i] = float(input(f'Digitia a temperatura média de {meses[i]}: '))
    os.system('cls')
    soma = soma + temperatura[i]
    i = i + 1
i = 0
media = soma//11 
while i < 11:
    if temperatura[i] > media:
        print(f'a temperatura {temperatura[i]} que ocorreu em {meses[i]} estava acima da média',end='')
        print()
    i = i + 1
print(f'A média anual de temperatura foi: {media}')