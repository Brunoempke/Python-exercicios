n1=float(input('qual a primeira nota:'))
n2=float(input('qual a segunda nota:'))
media= (n1+n2)/2
print('a media do aluno é {}'.format(media))
if media<=5:
    print('o aluno esta reprovado')
elif media > 5 and media < 6.9:
    print('o aluno esta de recuperação')
else:
    print('esta aprovado')

