resp='s'
media=quant=soma=maior=menor=0
while resp in 'Ss':
    num=int(input('qual numero? '))
    quant+=1
    soma+=num
    if quant == 1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor=num
    resp=str(input('quer continuar? [s/n] ')).upper() .strip()
    media=soma/quant
print('finalizado com {} numeros e a media foi {}'.format(quant,media))
print('o maior numero foi {} e o menor foi {}'.format(maior,menor))
