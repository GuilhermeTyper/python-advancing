import math
import os

qtd = float(input('Qauntos litros deseja colocar: '))
os.system('cls')
tipo = input('Qual o combustivel? (A) para álcool, (D) para diesel, ou (G) para gasolina: ')
os.system('cls')

if tipo == 'A':
    a = qtd * 3.89
    print(f'Valor a pagar: {a:.2f}')
elif tipo == 'D':
    d = qtd * 3.65
    print(f'Valor a pagar: {d:.2f}')
elif tipo == ('G'):
    g = qtd * 4.40
    print(f'Valor a pagar: {g:.2f}')
else:
    print('DIGITE UM VALOR VÁLIDO!!!')