from random import randint
from time import sleep
computador= randint(0,10)
print('=='*20)
print('pensei em um numero, tente adivinhar')
print('=='*20)
jogador=int(input('em que numero eu pensei:'))
print('processando...')
sleep(3)
if jogador== computador:
    print('parabens,voce me venceu')
else:
    print('eu venci, pensei no numero {}'.format(computador))

