distancia=int(input('digite a distancia da viagem'))
if distancia >=200:
    preço= distancia *0.50
else:
    preço= distancia * 0.45
print('voce pagara pela viagem {}'.format(preço))
