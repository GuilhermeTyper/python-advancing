# # isinstance
lista = ['nome',11,1.5,{1,2},(5,4),{'nome':'guilherme'}]

# for num, index in enumerate(lista):
#     if isinstance(index, set):
#         print(f"exite um set na lista na posição {num}")

# #hasattr
string = 'guilherme'
# resp1 = hasattr(lista,'upper')#verifica se existe o metodo para a lista
# print(resp1)#Saída será false, porque não existe um metodo upper pra listas
#getattr
print(getattr(string, "upper")())#verificando se existe o metodo upper para a variavel, e executando o mesmo ao mesmo tempo

#Outro jeito de verificar quais metodos exite para as variavél, é usando o dir(objeto) 

