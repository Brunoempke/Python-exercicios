casa=float(input('qual valor da casa?'))
salario=float(input('qual o salario?'))
anos=int(input('divide em quantos anos?'))
prestação= casa/ (anos*12)
minimo= salario*30/100
if prestação <= minimo:
    print('concedeu')
else:
    print('nao concedeu')
