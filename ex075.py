numeros=list()
while True:
    n=int(input('qual o valor?'))
    if n not in numeros:
        numeros.append(n)
    else:
        print('valor duplicado!')

    r=str(input('quer continuar? [s/n]')).strip() .upper() [0]
    if r in 'Nn':
        break
numeros.sort()
print(f'os valores adicionados foram {numeros}')


