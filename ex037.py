num=int(input('digite um numero:'))
print('''esolha uma das opcçoes
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
opção=int(input('qual opção escolhida:'))
if opção == 1:
    print('a conversao de {} é {}'.format(num,bin(num)))
elif opção == 2:
    print('a conversao de {} é {}'.format(num,oct(num)))
elif opção == 3:
    print('{} convertido é {}'.format(num,hex(num)))
else:
    print(' tente novamente ')

