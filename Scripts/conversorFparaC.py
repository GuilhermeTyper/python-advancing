import math
import os

temp = int(input("Digite a temperatura: "))
os.system('cls')

tip = input("Digite (F) para fahrenheit or (C) para Celsius: ").upper()
os.system('cls')

if tip == 'F':
    f = temp * 1.8 + 32
    print('A temperatura é:',f)
elif tip == 'C':
    c = (temp - 32)/1.8 
    print('A temperatura é:',c)
else:
    print('Valor Inválido!!!')

