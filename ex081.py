from random import randint
lista=list()
jogos=list()
quant=int(input('quantos jogos deseja?'))
tot= 1
while tot <= quant:
    cont=0
    while True:
        num=randint(0,60)
        if num not in lista:
            lista.append(num)
            cont+= 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')