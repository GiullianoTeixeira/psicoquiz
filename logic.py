from content.results import results as r
from text import *

# NOTE: respostas É UM DICIONÁRIO DA FORMA {tipo: peso}

# FIXME: IMPLEMENTAR A FUNÇÃO QUE RETORNA O INTERVALO DE CADA TIPO DE RESULTADO
def retornar_intervalo(respostas):
    return 

# FIXME: IMPLEMENTAR A FUNÇÃO QUE CALCULA O RESULTADO FINAL
def calcular_resultado(respostas):
    resultado = {}
    for key in respostas:
        resultado[key] = [None]
    
    print(respostas)

    return resultado
        

# NOTE: final_result É A FUNÇÃO ENVIADA PARA O CÓDIGO PRINCIPAL 
# E DEVE RETORNAR UMA LISTA COM RESULTADOS DE r 

def final_result(answers):
    return calcular_resultado(answers)