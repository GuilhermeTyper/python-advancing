def multiplication(tipo):
    def funcao(valor):
        return valor * tipo
    return funcao

dobro = multiplication(2)
triplo = multiplication(3)
quadruplo = multiplication(4)

while True:
    while True:
        user = input('Digite qual o numero: ')
        if user.isdigit():
            break
        else:
            print("por favor digite um valor válido!")
    print('qual a equaçaõ você deseja fazer?')
    resp = input('[d]obro [t]riplo [q]uadruplo: ')
    if resp == 'd':
      result = dobro(user)
    elif resp == 't':
      result = triplo
    elif resp == 'q':
      result = quadruplo
    else:
       print("impossivel fazer o calculo!")
    continuar = input('deseja continuar? [S/N]: ').upper()
    if continuar == 'S':
       continue 
    elif continuar == 'N':
       break
    else:
       print('Digite uma entrada válida!')
    
       
