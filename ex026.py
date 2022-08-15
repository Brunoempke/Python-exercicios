nome=str(input('digite seu nome')).upper().strip()
print('quantas vezes aparece a letra a: {}'.format(nome.count('A')))
print('a letra a aprece na {} posição'.format(nome.find('A')))
print('em que posição aparece a ultima letra a: {}'.format(nome.rfind('A')))
