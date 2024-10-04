class Mamifero:
  def emitir_som(self):
    pass
  
class Cachorro(Mamifero):
  def emitir_som(self):
    print("latido")

class Gato(Mamifero):
  def emitir_som(self):
        print("Miando")
  
cachorro = Cachorro()
gato = Gato()

lista = [cachorro,gato]

for index in lista:
    index.emitir_som()