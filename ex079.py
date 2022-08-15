temp=[]
princ=[]
maior=menor=0
while True:
    temp.append(str(input('nome:')))
    temp.append(float(input('quanto pesa:')))
    if {len(princ)} ==0:
        maior=menor=temp[1]
    else:
        if temp[1]>maior:
            maior=temp[1]
        if temp[1] < menor:
            menor=temp[1]
    princ.append(temp[:])
    temp.clear()
    resp=str(input('quer continuar?'))
    if resp in 'Nn':
        break
print(f'foram cadastradas {len(princ)} ao total')
print(f'o maior peso foi {maior} foi de ', end= '')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'o menor peso foi {menor}')
