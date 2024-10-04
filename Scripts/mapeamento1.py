lista = [10, 15, 21, 33, 42, 55]
expressao = lambda x : x * 2 + 3
result = list(map(expressao, lista))
print(result)
