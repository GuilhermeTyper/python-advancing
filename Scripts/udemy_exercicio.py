import os
def double():
    def number(num):
        return f'{num * 2}'
    return number

def triple():
    def number(num):
        tot = 0
        for i in range(4):
            tot = num * i
        return tot
    return number
def quadruple():
    def number(num):
        tot = 0
        for i in range(5):
            tot = num * i
        return tot
    return number

double = double()
triple = triple()
quadruple = quadruple()

print('What do you what do to?')
user_choice = input('[d]ouble [t]riple [q]uadruple: ')
os.system('cls')
user_num = int(input('what number do you want to see: '))
os.system('cls')

if user_choice == 'd':
    print(double(user_num))
elif user_choice == 't':
    print(triple(user_num))
elif user_choice == 'q':
    print(quadruple(user_num))
else:
    print('something is going wrong, pls try again!')
