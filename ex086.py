pessoa= dict()
galera= list()
soma=media=0
while True:
    pessoa.clear()
    pessoa ['nome']= str(input('nome:'))
    while True:
        pessoa['sexo'] = str(input('sexo [m/f]')).upper() [0]
        if pessoa['sexo'] in 'MF':
            break
        print('erro! digite somente m ou f')
    pessoa['idade']= int(input('idade:'))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp=str(input('quer continuar?')).upper() [0]
        if resp in 'SN':
            break
        print('erro! digite somente s ou n')
    if resp == 'N':
        break
print(galera)
print(f'ao todo temos {len(galera)} pessoas cadastradas')
media= soma/ len(galera)
print(f'a media é {media:.2f}')
print('as mulheres cadastradas são:', end= ' ')
for p in galera:
    if p['sexo']== 'F':
        print(f'{p["nome"]}',end= ' ')
print('pessoas com idade acima da media', end= ' ')
for p in galera:
    if p['idade'] >= media:
        print(f'{p["nome"]}')




