salario=float(input('digite o salario'))
if salario <=1250:
    novo= salario + (salario * 15 / 100)
else:
    novo= salario + (salario * 10 / 100)
print('o novo salario é {}'.format(novo))
