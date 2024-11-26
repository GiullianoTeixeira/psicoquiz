from content.results import results as r
from text import *

def calcular_resultado(respostas):
    if respostas[ansiedade] > 2:
        return r[1]
    elif respostas[exaustao_mental] > 2:
        return r[2]
    elif respostas[alto_para_raiva] > 2:
        return r[3]
    elif respostas[alto_para_tristeza] > 2:
        return r[4]
    elif respostas[voce_esta_bem] > 2:
        return r[5]
    else:
        return r[6]

def titulo_resultado(respostas):
    if respostas[ansiedade] > 2:
        return ansiedade
    elif respostas[exaustao_mental] > 2:
        return exaustao_mental
    elif respostas[alto_para_raiva] > 2:
        return alto_para_raiva
    elif respostas[alto_para_tristeza] > 2:
        return alto_para_tristeza
    elif respostas[voce_esta_bem] > 2:
        return voce_esta_bem
    else:
        return inconclusivo

def final_result(answers):
    return (calcular_resultado(answers), titulo_resultado(answers))