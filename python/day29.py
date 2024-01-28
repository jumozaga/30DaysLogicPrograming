def soma_digitos(num):
    return sum(int(digito) for digito in str(num))

num = int(input('Digite um número: '))
print('A soma dos dígitos do número é:', soma_digitos(num))
