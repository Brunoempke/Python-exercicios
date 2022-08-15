import random
n1=input('didite um aluno')
n2=input('digite outro')
n3=input('outro')
n4=input('outro')
lista=[n1,n2,n3,n4]
escolhido= random.choice(lista)
print('o escolhido foi {}'.format(escolhido))
