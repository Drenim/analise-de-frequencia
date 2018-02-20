import pprint
from collections import Counter

def obtem_linhas(path):
    with open(path, mode="r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    
    return linhas

def conta_letras(linhas):    
    contador = Counter()

    for linha in linhas:
        contador.update(linha.lower())

    return contador

if __name__ == '__main__':
    linhas = obtem_linhas("o-alienista.txt")
    contador = conta_letras(linhas)
    pprint.pprint(contador)



