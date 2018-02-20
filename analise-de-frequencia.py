import pprint
from collections import Counter

def obtem_linhas(path):
    with open(path, mode="r") as arquivo:
        linhas = arquivo.readlines()
    
    return linhas

def conta_letras(linhas):    
    contador = Counter()

    for linha in linhas:
        contador.update(linha.lower())

    return contador

def percentual_de_frequencia(relatorio, contador):
    total = sum(contador.values())
    
    for simbolo in contador:
        relatorio[simbolo]["Freq. percentual"] = (contador[simbolo] * 100) / total


def constroi_relatorio(contador):
    relatorio = dict()

    for simbolo in contador:
        relatorio[simbolo] = dict()

    percentual_de_frequencia(relatorio, contador)

    return relatorio

if __name__ == '__main__':
    linhas = obtem_linhas("o-alienista.txt")
    contador = conta_letras(linhas)
    pprint.pprint(constroi_relatorio(contador))




