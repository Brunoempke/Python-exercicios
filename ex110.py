def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except:
            print('ERRO, digite um numero inteiro valido')
            continue
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n=float(input(msg))
        except(ValueError, TypeError):
            print('digite um numero real valido')
            continue
        else:
            return n


num=leiaint('digite um numero inteiro:')
print(f'o numero foi {num}')

num=leiafloat('digite um numero real:')
print(f'o numero real foi {num}')






