def aumentar (preço, taxa):
    res= preço + (preço * taxa/100)
    return res


def diminuir (preço, taxa):
    res= preço - (preço * taxa/100)
    return res


def metade (preço):
    res= preço/2
    return res


def dobro(preço):
    res= preço * 2
    return res


def moeda(preço=0,moeda='R$'):
    return (f'{moeda}{preço:.2f}')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('analisando valor')
    print('-'*30)
    print(f'valor analisado: {moeda(preço)}')
    print(f'o dobro do preço é {dobro(preço)}')
    print(f'metade do preço é {metade(preço)}')

