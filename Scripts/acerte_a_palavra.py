
palavra_secreta = 'perfume'
letra_acertadas = '' #Essa variavel quando o programa chegar nela dentro loop, ele irá procurar a exixtencia dela no programa todo
while True:
    letra_digitada = input('Digite uma letra: ')
    if len(letra_digitada) > 1: #Caso o usuario digitar mais que 2 letras 
        print('Digite apena uma letra!')
        continue
    if letra_digitada in palavra_secreta: #Se a letra digitada for igual a letra da palavras secreta
        letra_acertadas += letra_digitada #A variavel letras_acertadas, está salvando as letras que o usuario já digitou e acertou
    palavras_formada = '' #Essa variavel será responsável por deixar a resposta na horinzontal
    for letra_secreta in palavra_secreta: #O index do for, letras_secretas, vai comparar o item da casa 1 da variavel palavre_secreta que seria a letra "p" 
        if letra_secreta in letra_acertadas: #Se o index for igual as letras acertadas ele irá mostra-las
            palavras_formada += letra_acertadas #Caso ele tenha acertado, a palavra_formada irá receber a letra acertada caso contrario, ela irá receber um asteristico 
        else:
            palavras_formada += '*'
    print(palavras_formada)

