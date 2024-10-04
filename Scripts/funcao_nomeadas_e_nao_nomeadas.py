def mult(*args):
    tot = 1
    for i in args:
        tot = tot * i
    return tot

print(mult(1,2,3,4,5))

def impar_par(num):
    multiplo = num % 2 == 0
    if multiplo:
        return f'{num} é par'
    return f'{num} é impar'

print(impar_par(3))
print(impar_par(5))
print(impar_par(12))
print(impar_par(16))

def saudacao(name):
    return f'{name} olá'

def executa(funcao,*args):#funcao nada mais é que a saudacao
    return funcao(*args)#vai retornar a funçaõ saudacao

print(executa(saudacao,'joão'))
print(executa(saudacao,'maria'))
