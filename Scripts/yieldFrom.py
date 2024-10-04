def gen1():
 yield 1
 yield 2
 yield 3

def gen2():
 yield from gen1()#quando o gen2 for executado ele irá fazer referencia ao gen1 aqui
 yield 4
 yield 5
 yield 6
 

gen = gen2()
for index in gen:
 print(index)
