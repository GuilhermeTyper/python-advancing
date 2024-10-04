import os
class Conta:
  def __init__(self, numero, titular):
    self.numero = numero
    self.titular = titular
    self.__saldo = 0
  @property
  def saldo(self):
      return self.__saldo
    
  def depositar(self,valor):
      if valor < 0:
         return "o valor deve ser maior quer 0"
      self.__saldo += valor
      return "deposito efetuado com sucesso!"

  def sacar(self,valor):
      if valor < 0:
         return "o valor deve ser maior quer 0"
      if valor > self.__saldo:
         return "saldo insulficiente para fazer essa operação"
      self.__saldo -= valor
      return "saque efetuando com suceeso!"
c1 = Conta(1,'guilherme')
c1.depositar(100)
print(c1.saldo)
# if __name__ == "__main__":
#   c1 = Conta(1,'guilherme')
#   while True:
#     print('O que deseja fazer?')
#     usuario = input('[P]egar denheiro [D]epositar [v]er saldo ou [S]air: ').upper()
#     if usuario == 'V':
#         os.system('cls')
#         print(c1.ver_saldo())
#     elif usuario == 'P':
#         os.system('cls')
#         valor = int(input('Digite o valor que será sacado: '))
#         print(c1.sacar(valor))
#     elif usuario == 'D':
#         os.system('cls')
#         valor = int(input('Digite o valor que será depositado: '))
#         print(c1.depositar(valor))
#     if usuario == 'S':
#         os.system('cls')
#         break
  # c1.depositar(300)
  # c1.ver_saldo()
  # print(c1.sacar(5000))
  # c1.ver_saldo()
  # print(vars(c1))