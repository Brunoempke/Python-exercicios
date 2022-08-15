n=list()
par=list()
impar=list()
while True:
    n.append(int(input('digite um valor:')))
    resp=str(input('quer continuar? [s/n]'))
    if resp in 'Nn':
        break
for i, v in enumerate(n):
    if v %2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(n)
print(f'os numeros impares sãp {impar}')
print(f'os numeros pares são {par}')
