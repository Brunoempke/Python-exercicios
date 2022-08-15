def maior(* num):
    cont=maior=0
    print('\nanalisando o valor passado!')
    for valor in num:
        print(f'{valor}',end= ' ')
        if cont == 0:
            maior=valor
        else:
            if cont > maior:
                maior=valor
        cont += 1
    print(f'foram analisados {cont} valores')
    print(f'o maior valor foi {maior}')


maior(2,3,4,5,6,7)
maior(5,8,2,5)

