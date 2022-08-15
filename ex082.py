ficha=list()
while True:
    nome=str(input('nome:'))
    nota1=float(input('nota 1:'))
    nota2=float(input('nota 2:'))
    media= (nota1 + nota2)/2
    ficha.append([nome,[nota1, nota2],media])
    resp=str(input('quer continuar?'))
    if resp in 'Nn':
        break
for i, a in enumerate(ficha):
    print(f'{a[0]} tirou {a[2]}')
while True:
    opc=int(input('qual aluno quer ver:'))
    if opc == 999:
        print('finalizado')
        break
    if opc <= len(ficha) -1:
        print(f'{ficha[opc][0]} tirou {ficha[opc][2]} ')

