n1=int(input('qual o primeiro valor:'))
n2=int(input('segundo valor:'))
n = 0
while n != 1:
 print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] finalizar''')
    n=int(input('qual sua opção?'))
    if n == 1:
        soma=n1+n2
        print('a soma é {}'.format(soma))
    elif n == 2:
        multiplicar=n1*n2
        print('multiplicação é {}'.format(multiplicar))
    elif n == 3:
        if n1>n2:
            maior=n1
        else:
            maior=n2
        print('entre {} e {} o maior é {}'.format(n1,n2,maior))
    elif n == 4:
        print('informe os numeros novamente')
        n1=int(input('qual primeiro valor'))
        n2=int(input('qual segundo valor'))
print('fim do programa')

