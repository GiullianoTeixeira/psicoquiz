from content.results import results as r
from text import *

# NOTE: respostas É UM DICIONÁRIO DA FORMA {tipo: peso}

def calcular_resultado(respostas):
    resultado = []
    if respostas[inconclusivo] >= 3:
        return [r[inconclusivo][0]]
    
    for tipo in respostas:
        if tipo == inconclusivo:
            pass
        elif respostas[tipo] > 10:
            resultado.append(r[tipo][1])
        elif respostas[tipo] <= 10:
            resultado.append(r[tipo][3])
        else:
            resultado.append(r[tipo][5])

    return resultado
            

def final_result(answers):
    return calcular_resultado(answers)