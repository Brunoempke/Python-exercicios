from datetime import date
atual=date.today().year
nasc=int(input('que ano voce nasceu?'))
idade= atual-nasc
print('voce tem {} anos'.format(idade))
if idade == 18:
    print('se alista vagabundo')
elif idade < 18:
    saldo=18-idade
    print('faltam {} anos porra!'.format(saldo))
    ano=atual+saldo
    print('devera se alistar em {} anos'.format(ano))
elif idade > 18:
    saldo= idade-18
    print('voce deveria se alistar há {} anos'.format(saldo))
    ano=atual-saldo
    print('seu alistamento foi em {}'.format(ano))
