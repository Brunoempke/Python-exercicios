nome=str(input('digite um nome')).strip()
print('nome em maiusculo é {}'.format(nome.upper()))
print('nome minusculo é {}'.format(nome.lower()))
print('o nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('o primeiro nome tem {} letras'.format(nome.find(' ')))