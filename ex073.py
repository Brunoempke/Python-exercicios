palavra= ('aprender','programar','lutar','beijar')
for p in palavra:
    print(f'\nna palavra {p.upper()} temos',end= ' ')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end= ' ')

