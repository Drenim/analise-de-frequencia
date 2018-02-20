import pprint
import csv
from collections import Counter, OrderedDict

def obtem_linhas(lista_de_paths):
    linhas = []
    for path in lista_de_paths:
        with open(path, mode="r") as arquivo:
            linhas += arquivo.readlines()
    
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

def salva_relatorio(relatorio):
    with open("relatorio.csv", mode="w", newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["Simbolo", "Freq. absoluta", "Freq. percentual"])
        
        for simbolo in relatorio:
            row = [simbolo, relatorio[simbolo]["Freq. absoluta"], 
                relatorio[simbolo]["Freq. percentual"]]
            writer.writerow(row)

if __name__ == '__main__':
    linhas = obtem_linhas(["textos-para-analise/o-alienista.txt", 
            "textos-para-analise/dom-casmurro.txt"])
    contador = conta_letras(linhas)
    relatorio = constroi_relatorio(contador)
    pprint.pprint(relatorio)
    salva_relatorio(relatorio)



