from content.results import results as r
from text import *

# pontos máximos:
# ansiedade = 180
# bem = 265
# exaustao mental = 224
# raiva = 168
# tristeza = 230
# inc = 120

def calcular_resultado(respostas):
    print(respostas)
    if respostas[exaustao_mental] > 130:
        return r[2]
    elif respostas[ansiedade] > 100:
        return r[1]
    elif respostas[alto_para_raiva] > 86:
        return r[3]
    elif respostas[alto_para_tristeza] > 120:
        return r[4]
    elif respostas[voce_esta_bem] > 120:
        return r[5]
    else:
        return r[6]
        
def titulo_resultado(respostas):
    if respostas[exaustao_mental] > 130:
        return exaustao_mental
    elif respostas[ansiedade] > 100:
        return ansiedade
    elif respostas[alto_para_raiva] > 86:
        return alto_para_raiva
    elif respostas[alto_para_tristeza] > 120:
        return alto_para_tristeza
    elif respostas[voce_esta_bem] > 120:
        return voce_esta_bem
    else:
        return inconclusivo

def final_result(answers):
    return (calcular_resultado(answers), titulo_resultado(answers))