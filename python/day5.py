def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)

num = int(input('Digite um número: '))
print('O fatorial do número é:', fatorial(num))
