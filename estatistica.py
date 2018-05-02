from collections import Counter
from math import floor, ceil, sqrt


def media(*args):
    return sum(args) / len(args)


def mediana(amostra):
    p = (len(amostra) + 1) / 2

    if len(amostra) % 2 == 0:
        md = (amostra[floor(p)] + amostra[ceil(p)]) / 2
    else:
        md = amostra[p]

    return md


def moda(amostra):
    contador = Counter(amostra)

    ultimo = list(contador.values())[0]
    iguais = True
    for i in contador.values():
        if ultimo != i:
            iguais = False
            break
        ultimo = i

    if iguais:
        return None
    else:
        moda = contador.most_common(1)[0][1]
        print(moda)
        moda = tuple(i for i in contador if contador[i] == moda)
        return moda


def quartis(amostra):
    n = len(amostra)
    if n % 2 == 0:
        p1 = (n + 2) / 4
        p2 = (2*n + 2) / 4
        p3 = (3*n + 2) / 4
    else:
        p1 = (n + 1) / 4
        p2 = (2*n + 2) / 4
        p3 = (3*n + 3) / 4

    return (amostra[p1], amostra[p2], amostra[p3])


def amplitude_total(amostra):
    return max(amostra) - min(amostra)


def amplitude_interquartilica(amostra):
    _quartis = quartis(amostra)
    return _quartis[2] - _quartis[0]


def desvio_medio_absoluto(amostra):
    _media = media(*amostra)
    desvios_absolutos = [abs(i - _media) for i in amostra]

    return sum(desvios_absolutos) / len(amostra)


def variancia(amostra):
    _media = media(*amostra)
    desvios_ao_quadrado = [(i - _media) ** 2 for i in amostra]
    return sum(desvios_ao_quadrado) / (len(amostra) - 1)


def desvio_padrao(amostra):
    _variancia = variancia(amostra)
    return sqrt(_variancia)


def coeficiente_de_variacao(amostra):
    _media = media(*amostra)
    _desvio_padrao = desvio_padrao(amostra)
    return (_desvio_padrao / _media) * 100
