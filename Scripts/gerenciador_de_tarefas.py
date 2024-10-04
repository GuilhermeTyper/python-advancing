#QPython utf-8
#lista de tarefas
#Windows,Unix,Linux e Mac

import os
#import androidhelper

#droid = androidhelper.Android()
def mostrar_tarefas(lista):
 for index,valor in enumerate(lista):
    print(f'{index}-{valor}')
    
def limpar_tela():
 if os.name == 'posix':
    return os.system('clear')
 elif os.name == 'nt':
    return os.system('cls')
 else:
    return('SO não é Unix, Linux,Mac ou Windows')

def validador_int(variavel):
    if variavel.isdigit():
       variavel = int(variavel)
       return variavel
    else:
       return -1
       
while True: #loop de sainda do programa

 #autenticacao da quantidade de tarefas
 while True:  
  qtd = input(f'digite quantas tarefas irá ser feita: ')
  qtd = validador_int(qtd)
  if qtd != -1:
     break
  limpar_tela()
  #droid.makeToast('digite a quantidade!')
  print('digite a quantidade')
  #fim da autenticação
   
 limpar_tela()
 
 #criando a lista de tarefas
 tarefas = list(quantidade for quantidade in range(0,qtd))
 for index, valor in enumerate(tarefas):
  tarefas[index] = input(f'digite qual será a {index}° tarefa: ')
 #fim da criação da lista de tarefas 
 
  limpar_tela()
  
 while True:#loop de controle de tarefas
 
 #autenticacao de tarefa
  while True:
     resp = input('você fez alguma tarefa? [S/N]: ').upper()
     limpar_tela()
     if resp == 'S':
        limpar_tela()
        break
     else:
         print('Você deve fazer as suas tarefas do dia!')
         #droid.makeToast('Você deve fazer as suas tarefas do dia!')
  #fim da autenticacao de tarefa
  
  mostrar_tarefas(tarefas)
  
  #excluir e autenticar as tarefa
  resp = input('qual o número da tarefa que você fez: ')
  resp = validador_int(resp)
  if resp != -1:
     del tarefas[resp]
  else:
     print('digite o número da tarefa!')
     mostrar_tarefas(tarefas)
  #fim do autenticador e deletar
  
  limpar_tela()
  
  #verificador de tarefas
  if len(tarefas) == 0:
     #droid.makeToast('Você não tem nunhuma tarefa para fazer!!')
     #droid.ttsSpeak('Você não tem nunhuma tarefa para fazer!!')
     print('Você não tem nunhuma tarefa para fazer!!')
     break
  #fim do verificador de tarefas
 
 #inicio do controle de encerramento 
 while True:   
   continuar = input('Deseja inserir novas tarefas[S/N]: ').upper()
   if continuar == 'N' or  continuar == 'S':
      break
   else:
     print('Digite uma entrada válida!')
     #droid.makeToast('Digite uma entrada válida!')
     limpar_tela()
 limpar_tela()
 if continuar == 'N':
    print('Aplicação encerrada!')
    break     
 #fim do controle de encerramento
