def ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

ano = int(input('Digite um ano: '))
if ano_bissexto(ano):
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')
