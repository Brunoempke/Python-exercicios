valor = float(input('qual o preço?'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('qual é a opção?'))
if opção == 1:
    total = valor - (valor * 10 / 100)
elif opção == 2:
    total = valor - (valor * 5 / 100)
elif opção ==3:
    total=valor
    parcela=valor/2
    print('sua compra sera parcelada em 2x ficara {}'.format(parcela))
elif opção ==4:
    total=valor+(valor*20/100)
    totalparc=int(input('quantas parcelas?'))
    parcela=total/totalparc
    print('o valor dividindo em {}x fica {}'.format(totalparc,parcela))
print('a compra de {} é {}'.format(valor, total))
