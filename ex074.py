listanum= []
maior=menor=0
for c in range (0,5):
    listanum.append(int(input('digite um valor')))
    if c ==0:
        maior=menor=listanum[c]
    else:
        if listanum[c] > maior:
            maior=listanum[c]
        if listanum[c]< menor:
            menor=listanum[c]
print(f'voce digitou os valores {listanum}')
print(f'o maior é {maior}')
print(f'o menor é {menor}')
