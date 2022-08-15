velocidade=float(input('qual a velocidade do carro'))
if velocidade >80:
    print('voce foi multado')
    multa= (velocidade-80) * 7
    print('a multa sera de {}'.format(multa))
else:
    print('dirija com segurança')

