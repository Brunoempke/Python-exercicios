from random import randint
numeros=list()

def sorteia(lista):
    for cont in range (0,5):
        n=(randint(1,10))
        lista.append(n)
        print(f'{n}',end=' ')


def somapar(lista):
    soma=0
    for valor in lista:
        if valor %2 == 0:
            soma+=valor
    print(f'a soma dos valores pares são {soma}')


sorteia(numeros)
somapar(numeros)
