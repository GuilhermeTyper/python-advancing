lista = [
{'nome': 'Luiz', 'sobrenome': 'miranda'},
{'nome': 'Maria', 'sobrenome': 'Oliveira'},
{'nome': 'Daniel', 'sobrenome': 'Silva'},
{'nome': 'Eduardo', 'sobrenome': 'Moreira'},
{'nome': 'Aline', 'sobrenome': 'Souza'},
]


lista.sort(key=lambda valor : valor['nome'])

for i in lista:
    print(i)