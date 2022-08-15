print('=='*20)
print('analisador de triangulo')
print('=='*20)
r1=float(input('digite um valor:'))
r2=float(input('digite outro valor:'))
r3=float(input('outro:'))
if r1< r2 + r3 and r2< r1+r3 and r3< r1 + r2:
    print('forma um triangulo')
else:
    print('nao forma um triangulo')

