def mdc(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print('O MDC dos números é:', mdc(num1, num2))
