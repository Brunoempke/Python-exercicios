def leiaint(msg):
    ok=False
    valor=0
    while True:
        n=str(input(msg)).strip()
        if n.isnumeric():
            valor= int(n)
            ok=True
        else:
            print('erro! digite um numero inteiro')
        if ok:
            break
    return valor


n=leiaint('digite um valor')
print(f'voce digitou o valor {n}')

