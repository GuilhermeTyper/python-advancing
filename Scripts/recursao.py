class Test:
    def __init__(self):
        self.__nome = ''
        self.cont = 0

    @property
    def nome(self):
        print('estou executando o getter...')
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        print('estou executando o setter...')
        self.__nome = novo_nome #acessando o valor privado manipulando o mesmo para o metodo público

t1 = Test()
t1.nome = 'guilherme' # executando o setter
print(t1.nome)#executando o getter
