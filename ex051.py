primeiro=int(input('primeiro:'))
razao=int(input('razão:'))
decimo= primeiro + (10-1)* razao
for c in range (primeiro,decimo+razao,razao):
    print('{}'.format(c),end= '-')

