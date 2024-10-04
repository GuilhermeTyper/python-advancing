import copy
d1 = dict(c1='1',c2='2',l1=[0,1,2])

d2 = copy.deepcopy(d1) #quando se trata de dados mutáveís, a lista original porerá ser alterada ao ser
#feito uma copia da mesma, pois o processador irá referenciar a copia com a original, para isso será
#necessário fazer uma cópia profunda da mesma.
d2['l1'][1] = 5846
print(d1)
print(d2)

