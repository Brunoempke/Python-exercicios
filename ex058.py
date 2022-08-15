primeiro=int(input('qual o primeiro termo: '))
razão=int(input('razão: '))
termo=primeiro
cont= 1
total= 0
mais= 10
while mais != 0:
    total= total + mais
    while cont <= total:
        print('{} -'.format(termo), end= ' ')
        termo += razão
        cont+=1
    print('pausa')
    mais=int(input('quer acrescentar quantos? '))
print('fim')
print('foi finalizado com {} '.format(total))
