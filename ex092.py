def voto (ano):
    from datetime import date
    atual= date.today().year
    idade= atual-ano
    if idade <=16:
        return f'com {idade} não vota!'
    elif idade <= 16 or idade < 18 or idade > 65:
        return f'com {idade} voto opcional'
    else:
        return f'com {idade} voto obrigatorio'


ano=int(input('que ano nasceu?'))
print(voto(ano))
