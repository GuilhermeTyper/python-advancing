def palindromo(texto):
    for index in range(len(texto)):
        if texto[index] != texto[-1-index]:
            return False
    return True
entradas = ['arara','elefante','radar','banana']
palindromos = []

for palavra in entradas:
    if(palindromo(palavra)):
        palindromos.append(palavra)
print(palindromos)