num=[[],[]]
valor=0
for c in range(0,7):
    valor=int(input('digite um valor:'))
    if valor %2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'os numeros pares sao {num[0]}')
print(f'os valores impares foram {num[1]}')
num.sort()
