# Definindo a classe pai
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

# Definindo a classe filha que herda de Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)  # Chama o construtor da classe pai
        self.portas = portas

    def exibir_informacoes(self):
        super().exibir_informacoes()  # Chama o método da classe pai
        print(f"Portas: {self.portas}")

# Criando uma instância da classe Carro
meu_carro = Carro("Toyota", "Corolla", 4)
meu_carro.exibir_informacoes()
