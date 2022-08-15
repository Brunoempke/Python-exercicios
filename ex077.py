valores=list()
while True:
    valores.append(int(input('qual valor?')))
    r=str(input('quer continuar [s/n]'))
    if r in 'Nn':
        break
print(f'digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'os valores decrescente são {valores}')
if 5 in valores:
    print('o 5 esta nos valores')
else:
    print('o 5 nao foi encontrado!')

