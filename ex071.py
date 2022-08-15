from random import randint
n= (randint (1,10),randint (1,10),randint (1,10),randint (1,10),randint (1,10))
print(f'os valores sorteados são:', end= ' ')
for numero in n:
    print(f'{numero}', end= ' ')
print(f'\n o maior valor sorteado foi {max(n)}')
print(f'o menor valor sorteado foi {min(n)}')

