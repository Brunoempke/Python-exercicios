tot18=toth=totm20=0
while True:
    idade=int(input('qual a idade: '))
    sexo=' '
    while sexo not in 'fm':
        sexo=str(input('qual sexo? ')).strip() .lower()[0]
    if idade >=18:
        tot18+=1
    if sexo == 'm':
        toth+=1
    if sexo == 'f' and idade <20:
        totm20+=1
    resp=' '
    while resp not in 'sn':
        resp=str(input('quer continuar? ')).strip() .lower()[0]
    if resp == 'n':
        break
print('cabou mos')
print(f'total de pessoas acima de 18: {tot18}')
print(f'total de homens: {toth}')
print(f'total de mulheres mais novas de 20: {totm20}')
