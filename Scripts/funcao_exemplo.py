def pede_idade(mensagem):
    """ função que retorna uma idade
    outras informações..."""
    idade = input(mensagem)
    idade = int(idade)
    return idade

idade = pede_idade('Digite a sua idade: ')

print(idade)