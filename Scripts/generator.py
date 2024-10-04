def generator(n=0, maximum=10):
    while True: 
        yield n  
        n+=1 
        if n > maximum:
          return 

gen = generator()
#print(next(gen))
#print(next(gen))#para fazer isso de uma forma sem ter que ficar chamando o next toda hora, é só adicionar o for abaixo

for i in gen:
    print(i)
# caso não tenha o yield no loop irá ocorrer um erro por ele não ser interável. 