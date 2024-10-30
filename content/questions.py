from text import *

# FIXME: DESCOMENTAR QUESTÕES, COMPLETAR COM PESOS DAS RESPOSTAS

questions = [
    ##############################################################################################
    # Q1
    ##############################################################################################
    {"question": q1["q"], "options": [
        {"text": q1["a1"], "traits": {
            ansiedade: 10,
            exaustao_mental: 1,
            alto_para_raiva: 5
        }},
        {"text": q1["a2"], "traits": {
            ansiedade: 20,
            exaustao_mental: 1,
            alto_para_raiva: 1
        }},
        {"text": q1["a3"], "traits": {
            alto_para_raiva: 1,
            alto_para_tristeza: 1
        }},
        {"text": q1["a4"], "traits": {
            alto_para_tristeza: 1,
            voce_esta_bem : 1
        }},
        {"text": q1["a5"], "traits": {
            inconclusivo: 1
        }}
    ]},
    ##############################################################################################
    # Q2
    ##############################################################################################
    {"question": q2["q"], "options": [
        {"text": q2["a1"], "traits": {
            ansiedade: 1,
            exaustao_mental: 1
        }},
        {"text": q2["a2"], "traits": {
            exaustao_mental: 1,
            alto_para_raiva: 1
        }},
        {"text": q2["a3"], "traits": {
            alto_para_raiva: 1,
            alto_para_tristeza: 1
        }},
        {"text": q2["a4"], "traits": {
            alto_para_tristeza: 1,
            voce_esta_bem : 1
        }},
        {"text": q2["a5"], "traits": {
            inconclusivo: 1
        }}
    ]},
    ##############################################################################################
    # Q3
    ##############################################################################################
    {"question": q3["q"], "options": [
        {"text": q3["a1"], "traits": {
            ansiedade: 1,
            exaustao_mental: 1
        }},
        {"text": q3["a2"], "traits": {
            exaustao_mental: 1,
            alto_para_raiva: 1
        }},
        {"text": q3["a3"], "traits": {
            alto_para_raiva: 1,
            alto_para_tristeza: 1
        }},
        {"text": q3["a4"], "traits": {
            alto_para_tristeza: 1,
            voce_esta_bem : 1
        }},
        {"text": q3["a5"], "traits": {
            inconclusivo: 1
        }}
    ]},
    
    # ##############################################################################################
    # # Q4
    # ##############################################################################################
    # {"question": q4["q"], "options": [
    #     {"text": q4["a1"], "traits": {
    #         ansiedade: 1,
    #         exaustao_mental: 1
    #     }},
    #     {"text": q4["a2"], "traits": {
    #         exaustao_mental: 1,
    #         alto_para_raiva: 1
    #     }},
    #     {"text": q4["a3"], "traits": {
    #         alto_para_raiva: 1,
    #         alto_para_tristeza: 1
    #     }},
    #     {"text": q4["a4"], "traits": {
    #         alto_para_tristeza: 1,
    #         voce_esta_bem : 1
    #     }},
    #     {"text": q4["a5"], "traits": {
    #       inconclusivo: 1
    #     }}
    # ]},
    # ##############################################################################################
    # # Q5
    # ##############################################################################################
    # {"question": q5["q"], "options": [
    #     {"text": q5["a1"], "traits": {
    #         ansiedade: 1,
    #         exaustao_mental: 1
    #     }},
    #     {"text": q5["a2"], "traits": {
    #         exaustao_mental: 1,
    #         alto_para_raiva: 1
    #     }},
    #     {"text": q5["a3"], "traits": {
    #         alto_para_raiva: 1,
    #         alto_para_tristeza: 1
    #     }},
    #     {"text": q5["a4"], "traits": {
    #         alto_para_tristeza: 1,
    #         voce_esta_bem : 1
    #     }},
    #     {"text": q5["a5"], "traits": {
    #       inconclusivo: 1
    #     }}
    # ]},
    # ##############################################################################################
    # # Q6
    # ##############################################################################################
    # {"question": q6["q"], "options": [
    #     {"text": q6["a1"], "traits": {
    #         ansiedade: 1,
    #         exaustao_mental: 1
    #     }},
    #     {"text": q6["a2"], "traits": {
    #         exaustao_mental: 1,
    #         alto_para_raiva: 1
    #     }},
    #     {"text": q6["a3"], "traits": {
    #         alto_para_raiva: 1,
    #         alto_para_tristeza: 1
    #     }},
    #     {"text": q6["a4"], "traits": {
    #         alto_para_tristeza: 1,
    #         voce_esta_bem : 1
    #     }},
    #     {"text": q6["a5"], "traits": {
    #       inconclusivo: 1
    #     }}
    # ]},
    # ##############################################################################################
    # # Q7
    # ##############################################################################################
    # {"question": q7["q"], "options": [
    #     {"text": q7["a1"], "traits": {
    #         ansiedade: 1,
    #         exaustao_mental: 1
    #     }},
    #     {"text": q7["a2"], "traits": {
    #         exaustao_mental: 1,
    #         alto_para_raiva: 1
    #     }},
    #     {"text": q7["a3"], "traits": {
    #         alto_para_raiva: 1,
    #         alto_para_tristeza: 1
    #     }},
    #     {"text": q7["a4"], "traits": {
    #         alto_para_tristeza: 1,
    #         voce_esta_bem : 1
    #     }},
    #     {"text": q7["a5"], "traits": {
    #       inconclusivo: 1
    #     }}
    # ]},
    # ##############################################################################################
    # # Q8
    # ##############################################################################################
    # {"question": q8["q"], "options": [
    #     {"text": q8["a1"], "traits": {
    #         ansiedade: 1,
    #         exaustao_mental: 1
    #     }},
    #     {"text": q8["a2"], "traits": {
    #         exaustao_mental: 1,
    #         alto_para_raiva: 1
    #     }},
    #     {"text": q8["a3"], "traits": {
    #         alto_para_raiva: 1,
    #         alto_para_tristeza: 1
    #     }},
    #     {"text": q8["a4"], "traits": {
    #         alto_para_tristeza: 1,
    #         voce_esta_bem : 1
    #     }},
    #     {"text": q8["a5"], "traits": {
    #       inconclusivo: 1
    #     }}
    # ]},
    # ##############################################################################################
    # # Q9
    # ##############################################################################################
    # {"question": q9["q"], "options": [
    #     {"text": q9["a1"], "traits": {
    #         ansiedade: 1,
    #         exaustao_mental: 1
    #     }},
    #     {"text": q9["a2"], "traits": {
    #         exaustao_mental: 1,
    #         alto_para_raiva: 1
    #     }},
    #     {"text": q9["a3"], "traits": {
    #         alto_para_raiva: 1,
    #         alto_para_tristeza: 1
    #     }},
    #     {"text": q9["a4"], "traits": {
    #         alto_para_tristeza: 1,
    #         voce_esta_bem : 1
    #     }},
    #     {"text": q9["a5"], "traits": {
    #       inconclusivo: 1
    #     }}
    # ]},
    # ##############################################################################################
    # # Q10
    # ##############################################################################################
    # {"question": q10["q"], "options": [
    #     {"text": q10["a1"], "traits": {
    #         ansiedade: 1,
    #         exaustao_mental: 1
    #     }},
    #     {"text": q10["a2"], "traits": {
    #         exaustao_mental: 1,
    #         alto_para_raiva: 1
    #     }},
    #     {"text": q10["a3"], "traits": {
    #         alto_para_raiva: 1,
    #         alto_para_tristeza: 1
    #     }},
    #     {"text": q10["a4"], "traits": {
    #         alto_para_tristeza: 1,
    #         voce_esta_bem : 1
    #     }},
     #     {"text": q10["a5"], "traits": {
    #       inconclusivo: 1
    #     }}
    # ]},
    # ##############################################################################################
    # # Q11
    # ##############################################################################################
    # {"question": q11["q"], "options": [
    #     {"text": q11["a1"], "traits": {
    #         ansiedade: 1,
    #         exaustao_mental: 1
    #     }},
    #     {"text": q11["a2"], "traits": {
    #         exaustao_mental: 1,
    #         alto_para_raiva: 1
    #     }},
    #     {"text": q11["a3"], "traits": {
    #         alto_para_raiva: 1,
    #         alto_para_tristeza: 1
    #     }},
    #     {"text": q11["a4"], "traits": {
    #         alto_para_tristeza: 1,
    #         voce_esta_bem : 1
    #     }},
     #     {"text": q11["a5"], "traits": {
    #       inconclusivo: 1
    #     }}
    # ]},
    # ##############################################################################################
    # # Q12
    # ##############################################################################################
    # {"question": q12["q"], "options": [
    #     {"text": q10["a1"], "traits": {
    #         ansiedade: 1,
    #         exaustao_mental: 1
    #     }},
    #     {"text": q12["a2"], "traits": {
    #         exaustao_mental: 1,
    #         alto_para_raiva: 1
    #     }},
    #     {"text": q12["a3"], "traits": {
    #         alto_para_raiva: 1,
    #         alto_para_tristeza: 1
    #     }},
    #     {"text": q12["a4"], "traits": {
    #         alto_para_tristeza: 1,
    #         voce_esta_bem : 1
    #     }},
     #     {"text": q12["a5"], "traits": {
    #       inconclusivo: 1
    #     }}
    # ]}
]