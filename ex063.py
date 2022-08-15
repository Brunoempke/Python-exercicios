soma=cont=0
while True:
    num=int(input('digite um numero: '))
    if num == 999:
        break
    soma+=num
    cont+= 1
print(f'os {cont} somam {soma}')
