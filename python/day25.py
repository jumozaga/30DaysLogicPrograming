def conta_palavras(texto):
    palavras = texto.lower().split()
    contagem = {}
    for palavra in palavras:
        if palavra not in contagem:
            contagem[palavra] = 1
        else:
            contagem[palavra] += 1
    return contagem

texto = input('Digite um texto: ')
contagem = conta_palavras(texto)
for palavra, quantidade in contagem.items():
    print('A palavra "{}" aparece {} vezes no texto'.format(palavra, quantidade))
