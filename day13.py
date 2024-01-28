def conta_palavras(texto, palavra):  
    return texto.lower().split().count(palavra.lower())
  
texto = input('Digite um texto: ')
palavra = input('Digite uma palavra: ')
print('A palavra "{}" aparece {} vezes no texto'.format(palavra,conta_palavras(texto, palavra)))



# texto = 'De um ditado "Num ninho de mafagafos 5 mafagafinhos há, um bom de mafagafos será'
# palavra = 'mafagafos'