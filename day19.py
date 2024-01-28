def eratosthenes(n):
    primes = [True for _ in range(n+1)]
    p = 2
    while p * p <= n:
        if primes[p] == True:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    for p in range(2, n):
        if primes[p]:
            print(p)

num = int(input('Digite um número: '))
eratosthenes(num)
