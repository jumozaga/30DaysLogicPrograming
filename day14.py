def raiz_newton(num, precisao=0.0001):
    x = num
    while abs(x - num / x) > precisao:
        x = (x + num / x) / 2
    return round(x, 2)

num = float(input('Digite um número: '))
print('A raiz quadrada do número é:', raiz_newton(num))
