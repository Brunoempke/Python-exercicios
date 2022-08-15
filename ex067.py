tot=totmil=cont=menor=0
while True:
    produto=str(input('qual o produto:'))
    valor=float(input('qual o preço?'))
    cont+=1
    tot+= valor
    if valor > 1000:
        totmil+=1
    if cont == 1:
        menor=valor
    else:
        if valor < menor:
            menor=valor
    resp= ' '
    while resp not in 'ns':
        resp=str(input('quer continuar?')).strip().lower()[0]
    if resp == 'n':
        break
print('cabou mos')
print(f'no total foram {tot} reais')
print(f'temos {totmil} produtos acima do valor de 1000')
print(f'o produto mais barato custa {menor}')
