frase=str(input('digite a frase:')) .strip() .upper()
palavra= frase.split()
junto='' .join(palavra)
inverso= junto [::-1]
if inverso == junto:
    print('palindromo')
else:
    print('nao é palindromo')

