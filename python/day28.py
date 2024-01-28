def gerar_primos(limite):
    primos = []
    for num in range(2, limite + 1):
        if all(num % i != 0 for i in range(2, num)):
            primos.append(num)
    return primos

limite = int(input('Digite um limite: '))
print('Os números primos até o limite são:', gerar_primos(limite))
