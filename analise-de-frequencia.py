import pprint
from collections import Counter, OrderedDict

def obtem_linhas(path):
    with open(path, mode="r") as arquivo:
        linhas = arquivo.readlines()
    
    return linhas

def conta_letras(linhas):    
    contador = Counter()

    for linha in linhas:
        linha_limpa = ''
        for char in linha:
            if char.isalpha():
                linha_limpa += char
        
        contador.update(linha_limpa.lower())

    return contador

def percentual_de_frequencia(relatorio, contador):
    total = sum(contador.values())
    
    for simbolo in contador:
        relatorio[simbolo]["Freq. percentual"] = (contador[simbolo] * 100) / total

def frequencia_absoluta(relatorio, contador):
    for simbolo in contador:
        relatorio[simbolo]["Freq. absoluta"] = contador[simbolo]

def constroi_relatorio_ordenado(relatorio, chave):
    iter_relatorio = relatorio.items()
    iter_relatorio = sorted(iter_relatorio, key=lambda simbolo: simbolo[1][chave])
    iter_relatorio = list(iter_relatorio)
    iter_relatorio.reverse()

    relatorio_ord = OrderedDict()
    for simbolo in iter_relatorio:
        relatorio_ord[simbolo[0]] = simbolo[1]

    return relatorio_ord

def constroi_relatorio(contador):
    relatorio = dict()

    for simbolo in contador:
        relatorio[simbolo] = dict()

    frequencia_absoluta(relatorio, contador)
    percentual_de_frequencia(relatorio, contador)

    relatorio = constroi_relatorio_ordenado(relatorio, "Freq. absoluta")

    return relatorio


if __name__ == '__main__':
    linhas = obtem_linhas("o-alienista.txt")
    contador = conta_letras(linhas)
    pprint.pprint(constroi_relatorio(contador))




