def ficha (jog='<desconhecido>',gol=0):
    print(f'o jogador {jog} fez {gol} gol(s)')


n=str(input('nome do jogador:'))
g=str(input('quantos gols:'))
if g.isnumeric():
    g=int(g)
else:
    g=0
if n.strip == '':
    ficha(gol=g)
else:
    ficha(n,g)
