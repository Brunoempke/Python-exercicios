soma=0
cont=0
for c in range(1,10,3):
    num=int(input('digite o {}º valor'.format(c)))
    if num % 2 ==0:
        soma= soma + num
        cont= cont + 1
print('informou {} numeros pares e a soma é {}'.format(cont,soma))
