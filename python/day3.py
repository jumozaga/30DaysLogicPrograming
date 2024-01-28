def verifica_par_impar(num):
    if num % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'

num = int(input('Digite um número: '))
print('O número é:', verifica_par_impar(num))
