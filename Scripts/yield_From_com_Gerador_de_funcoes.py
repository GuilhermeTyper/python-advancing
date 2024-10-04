def gen1():
    yield 1
    yield 2
    yield 3


def gen3():
    yield 10
    yield 20
    yield 30


def gen2(gen):
    yield from gen()  # quando o gen2 executar aqui ele irá fazer referencia ao gen que foi passado no parametro
    yield 4
    yield 5
    yield 6


gen = gen2(gen3)
for index in gen:
    print(index)
