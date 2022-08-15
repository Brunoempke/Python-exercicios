peso=float(input('qual seu peso?'))
altura=float(input('qual sua altura?'))
imc= peso /(altura**2)
print('pesando {} e medindo {}...'.format(peso,altura),end=' ')
if imc < 18.5:
    print('abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('peso ideal')
elif imc >= 25 and imc < 30:
    print('sobrepeso')
elif imc >= 30 and imc <= 40:
    print('obeso meu fi')
elif imc > 40:
    print('obeso demais, vai morrer')

