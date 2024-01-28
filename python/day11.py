def anagrama(string1, string2):
    return sorted(string1.lower()) == sorted(string2.lower())

string1 = input('Digite a primeira string: ')
string2 = input('Digite a segunda string: ')
if anagrama(string1, string2):
    print('As palavras são anagramas')
else:
    print('As palavras não são anagramas')
