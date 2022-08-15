sexo=str(input('informe seu sexo:')).strip() .lower()
while sexo not in 'mf':
    sexo=str(input('invalido, digite novamente:')) .strip() .lower()
print('o sexo {} foi registrado com sucesso!'.format(sexo))
