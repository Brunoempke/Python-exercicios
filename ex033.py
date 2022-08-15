a=int(input('digite um valor'))
b=int(input('digite outro valor'))
c=int(input('outro'))
#verificando menor valor
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
#verificando o maior
maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print('o maior numero é {} e o menor é {}'.format(maior,menor))
