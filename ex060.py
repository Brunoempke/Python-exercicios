num=soma=cont=0
num=int(input('qual numero? [999 encerra!] :'))
while num != 999:
    soma+=num
    cont+=1
    num=int(input('qual numero? [999 encerra!]: '))
print('digitou {} numeros e a soma deu {}'.format(cont,soma))
print('acabou putinha')
