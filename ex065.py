from random import randint
v=0
while True:
    jogador=int(input('qual valor: '))
    computador = randint(0,10)
    total= computador + jogador
    tipo = ' '
    while tipo not in 'pi':
        tipo=str(input('impar ou par?')).strip() .lower()[0]
    print('voce jogou {} e o comptador {}, resultado = {}'.format(jogador,computador,total))
    if tipo == 'p':
        if total %2 == 0:
            print('voce ganhou!')
            v+=1
        else:
            print('computador ganhou!')
            break
    elif tipo == 'i':
        if total %2==1:
            print('voce venceu!')
            v+=1
        else:
            print('computador venceu!')
            break
print(f'voce vence {v} vezes!')
