car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}

owner = {
 'nome': 'taylor',
 'sobrenome' : 'curry'
}

building = {**car,**owner}# unindo um dicionário no outro dicionário

def mostro_argumentos_nomeados(*args,**kwargs): #fazendo o empacontamento de dicionário
 for chave,valor in kwargs.items():
  print(chave,valor)
  
mostro_argumentos_nomeados(**car)#desenpacotamento de um dicionário já criado com uma função