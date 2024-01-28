def verifica_primo(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

num = int(input('Digite um número: '))
if verifica_primo(num):
    print(f'O {num} é primo')
else:
    print(f'O {num} não é primo')
