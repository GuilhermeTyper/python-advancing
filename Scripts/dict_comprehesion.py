produtos = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor*10 #sempre tem que ser com 2 pontos ao invés da vírgula
    if isinstance(valor,float) else valor#verifica se o valor é uma float,
    #caso ele seja, ele irá retorna o valor multiplicado por 10 
    for chave, valor in produtos.items()
}

print(dc)