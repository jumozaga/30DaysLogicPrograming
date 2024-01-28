def anagrama(string1, string2):
    return sorted(string1.upper()) == sorted(string2.upper())

string1 = input('Digite a primeira string: ')
string2 = input('Digite a segunda string: ')
if anagrama(string1, string2):
    print('As strings são anagramas')
else:
    print('As strings não são anagramas')
