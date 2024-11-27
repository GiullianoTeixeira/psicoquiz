##############################################################################################
# TRAITS
##############################################################################################
ansiedade = "Ansiedade"
exaustao_mental = "Exaustão Mental"
alto_para_raiva = "Alto para Raiva"
alto_para_tristeza = "Alto para Tristeza"
voce_esta_bem  = "Você está bem!"
inconclusivo = "Inconclusivo"

traits = [ansiedade, exaustao_mental, alto_para_raiva, alto_para_tristeza, voce_esta_bem, inconclusivo]



##############################################################################################
# QUESTIONS AND ANSWERS
##############################################################################################
q1 = {
    "q": "Como você anda ultimamente?",
    "a1": "Ótimo",
    "a2": "Bem",
    "a3": "Ruim",
    "a4": "Péssimo",
    "a5": "Não sei dizer"
}

q2 = {
    "q": "Você tem notado mudanças repentinas em seu humor recentemente?",
    "a1": "Não, nenhuma",
    "a2": "Raramente, em situações atípicas",
    "a3": "Com certa frequência, por conta de coisas não importantes",
    "a4": "Muitas vezes, (quase) todos os dias",
    "a5": "Não sei dizer"
}

q3 = {
    "q": "Você tem se sentido sobrecarregado ultimamente?",
    "a1": "Não",
    "a2": "Raramente",
    "a3": "Às vezes",
    "a4": "Muitas vezes",
    "a5": "Não sei dizer"
}

q4 = {
    "q": "Você fez algo que te deixou animado?",
    "a1": "Sim, muitas vezes",
    "a2": "Sim, algumas vezes",
    "a3": "Raramente",
    "a4": "Não, nenhuma",
    "a5": "Não sei dizer",
}

q5 = {
    "q": "Você tem se sentido cansado ultimamente?",
    "a1": "Não",
    "a2": "Raramente",
    "a3": "Às vezes",
    "a4": "Muitas vezes", 
    "a5": "Não sei dizer",
}

q6 = {
    "q": "Você tem se sentido desmotivado ultimamente?",
    "a1": "Não",
    "a2": "Raramente",
    "a3": "Às vezes",
    "a4": "Muitas vezes",
    "a5": "Não sei dizer",
}

q7 = {
    "q": "Você está preocupado com o que os outros estão pensando de você?",
    "a1": "Não",
    "a2": "Raramente",
    "a3": "Às vezes",
    "a4": "Muitas vezes",
    "a5": "Não sei dizer",
}

q8 = {
    "q":" Você está se sentindo sozinho ultimamente?",
    "a1": "Não",
    "a2": "Raramente",
    "a3": "Às vezes",
    "a4": "Muitas vezes",
    "a5": "Não sei dizer",
}

q9 = {
    "q": "Você tem se sentido triste ultimamente?",
    "a1": "Não",
    "a2": "Raramente",
    "a3": "Às vezes",
    "a4": "Muitas vezes",
    "a5": "Não sei dizer",
}

q10 = {
    "q": 'Você tem se sentido irritado ultimamente?',
    "a1": "Não",
    "a2": "Raramente",
    "a3": "Às vezes",
    "a4": "Muitas vezes",
    "a5": "Não sei dizer",
}


q11 = {
    "q": "Você tem se sentido entediado?",
    "a1": "Não",
    "a2": "Raramente",
    "a3": "Às vezes",
    "a4": "Muitas vezes",
    "a5": "Não sei dizer",
}


q12 = {
    "q": "Alguma coisa te deixou com raiva recentemente?",
    "a1": "Não",
    "a2": "Raramente",
    "a3": "Às vezes",
    "a4": "Muitas vezes",
    "a5": "Não sei dizer",
}



##############################################################################################
# RESULTS
##############################################################################################
res_ansiedade = [
    "Suas respostas indicam que você está com altos níveis em ansiedade",
    "Você pode estar preocupado preocupado com eventos futuros",
    "Orientamos que você:",
    "- tente identificar o que está te preocupando hoje",
    "- faça algo que te \"prenda\" ao aqui e agora, como assistir a um filme, ler um bom livro, ou até sair com seus amigos",
    "- caso persista, procure um especialista para te orientar e cuidar da sua saúde mental",
    "Lembre-se: pode dar tudo certo, o erro é só um talvez!"
]
res_exaustao_mental = [
    "Suas respostas indicam que você está exausto mentalmente",
    "Você pode estar cansado de sua rotina e estressado com problemas pessoais",
    "Orientamos que você:",
    "- tente identificar o porquê de estar estressado e cansado",
    "- faça algo que você goste, mas que não precise cansar muito a mente, como assistir a um filme, sair com seus amigos, ou até tomar um banho relaxante",
    "- caso persista, procure um especialista para te orientar e cuidar da sua saúde mental",
    "Lembre-se: você tem que descansar, não precisa carregar tudo nas costas!"
]
res_alto_para_raiva = [
    "Suas respostas indicam que você está com a raiva muito aflorada",
    "Você pode estar irritado com a atitude de alguém ou com algo que aconteceu",
    "Orientamos que você:",
    "- tente identificar o porquê de estar irritado",
    "- caso seja por alguém, recomendamos que você tente conversar com ele(a)",
    "- caso seja por algo, recomendamos que você faça coisas que relaxem, como um banho relaxante, comer algo que gosta, ou até tomar um sorvete",
    "Lembre-se: há coisas que não estão no nosso controle"
    ]
res_alto_para_tristeza = [
    "Suas respostas indicam que você está muito magoado",
    "Você pode estar triste com alguém, com algo ou consigo mesmo",
    "Orientamos que você:",
    "- tente identificar o porquê de estar triste",
    "- caso seja por alguém, recomendamos que você tente conversar com ele(a)",
    "- caso seja por algo, recomendamos que você faça coisas que você goste e te alegrem, pratique um hobbie",
    "Lembre-se: sinta sua tristeza, mas não deixe ela tomar conta, tudo bem não estar sempre bem!"
]
res_voce_esta_bem = [
    "Suas respostas indicam que você está aparentemente bem",
    "Apesar de ter alguns problemas, você não está deixando isso te afetar",
    "Orientamos que você:",
    "- continue cuidando da sua saúde mental",
    "Lembre-se: estar bem não é um motivo para parar de se cuidar!"
]
res_inconclusivo = [
    "Não conseguimos medir como você está sentindo, talvez devido a muitas respostas \"não sei dizer\".",
    "Você pode estar confuso com seus sentimentos, tente avaliá-los para entender melhor oque está sentindo.",
    "Orientamos que você:",
    "- converse com um amigo, ou procure um especialista para te orientar e te ajudar a se entender melhor" 
]