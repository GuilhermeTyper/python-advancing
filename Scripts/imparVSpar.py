import math
import os

num = int(input("Qual o número você quer verificar? "))

resp = num%2
if num%2 != 1:
    print(" O NUMERO É PAR!!!",resp)
else:
    print('O número é impar',resp)