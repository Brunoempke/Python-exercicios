from time import sleep

def contador (i,f,p):
    print(f'contar de {i} ate {f} de {p} em {p}')
    if i < f:
        cont= i
        while cont <= f:
            print(f'{cont}', end= ' ', flush=True)
            cont+= p
            sleep(0.5)
        print('fim')
    else:
        cont= i
        while cont >= f:
            print(f'{cont}', end= ' ', flush=True)
            cont-= p
            sleep(0.5)
        print('fim')


contador(1,10,2)
contador(10,-10,2)
print('sua vez!')
ini=int(input('inicio:'))
fim=int(input('fim:'))
pas=int(input('passo:'))
contador(ini,fim,pas)

