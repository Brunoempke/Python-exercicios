from random import randint
computador= randint(0,10)
print('adivinhe que numero estou pensando')
acertou = False
palpite= 0
while not acertou:
    jogador=int(input('qual seu palpite?'))
    palpite+= 1
    if jogador == computador:
        acertou=True
    else:
        if jogador < computador:
            print('mais!')
        if jogador > computador:
            print('menos!')
print('acertou com {} tentativas'.format(palpite))
