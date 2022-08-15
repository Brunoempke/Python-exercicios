from datetime import date
atual=date.today().year
anos=int(input('em que ano nasceu?'))
idade=atual-anos
print('quem nasceu em {} tem {}'.format(anos,idade))
if idade <=10:
    print('mirim')
elif idade > 10 and idade <=17:
    print('junior')
elif idade> 17:
    print('senior')
