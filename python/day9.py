def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input('Digite a temperatura em Celsius: '))
print('A temperatura em Fahrenheit é:', celsius_para_fahrenheit(celsius))
