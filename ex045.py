from random import randint
itens= ('pedra','papel','tesoura')
computador= randint (0,2)
print('''opções
[0] pedra
[1] papel
[2] tesoura''')
jogador=int(input('qual opção?'))
print('o computador jogou {}'.format(itens[computador]))
print('o jogador jogador jogou {}'.format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador vence')
    elif jogador == 2:
        print('computador vence!')
if computador == 1:
    if jogador == 1:
        print('empate')
    elif jogador == 0:
        print('computador vence')
    elif jogador == 2:
        print('jogador vence')
if computador == 2:
    if jogador == 2:
        print('empate')
    elif jogador == 1:
        print('jogador vence')
    elif jogador == 0:
        print('computador vence')

