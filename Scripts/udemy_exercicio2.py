def multplicador(multiplicador):
    def numero(numero):
        return numero * multiplicador
    return numero

duplicar = multplicador(2)
triplcar = multplicador(3)
quadruplicar = multplicador(4)
print(duplicar(2))
print(triplcar(2))
print(quadruplicar(2))

#closure exemplo!