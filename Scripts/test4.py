#-*-coding:utf8;-*-
#qpy:console

def exibe(v,n):
 i = 0
 while i < n:
  print(v[i],end=' ')
  i += 1
 print('\n')
 return 

def troca(v,i,j):
 v[i],v[j] = v[j],v[i]
 return 

def empurrar(v,n):
 i = 0
 while i < n -1:
  if v[i] > v[i+1]:
   troca(v,i,i+1)
  i += 1
  return 
  
def bubble_sort(v,n):
 exibe(v,n)
 tam = n
 while tam > 1:
  empurrar(v,tam)
  exibe(v,tam)
  tam -= 1
  exibe(v,n)
  return 
 
bubble_sort([40,20,50,30,10],5)