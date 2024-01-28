def pi_leibniz(n):
    pi = 0
    for k in range(n):
        pi += ((-1)**k) / (2*k + 1)
    return pi * 4

n = int(input('Digite um número: '))
print('O valor de π calculado com {} termos da série de Leibniz é aproximadamente:'.format(n), pi_leibniz(n))
