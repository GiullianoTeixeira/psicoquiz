from text import *

# : DESCOMENTAR QUESTÕES, COMPLETAR COM PESOS DAS RESPOSTAS

questions = [
    ##############################################################################################
    # Q1
    ##############################################################################################
    {"question": q1["q"], "options": [
        {"text": q1["a1"], "traits": {
            voce_esta_bem: 20,
            
        }},
        {"text": q1["a2"], "traits": {
            ansiedade: 2,
            exaustao_mental: 2,
            alto_para_raiva: 2,
            alto_para_tristeza: 2,
            voce_esta_bem: 10,
            inconclusivo:0,
        }},
        {"text": q1["a3"], "traits": {
            ansiedade: 10,
            exaustao_mental: 15,
            alto_para_raiva: 8,
            alto_para_tristeza: 20,
            voce_esta_bem: 0,
            inconclusivo:0,
        }},
        {"text": q1["a4"], "traits": {
            ansiedade: 10,
            exaustao_mental: 15,
            alto_para_raiva: 10,
            alto_para_tristeza: 15,
            voce_esta_bem: 0,
            inconclusivo:0,
        }},
        {"text": q1["a5"], "traits": {
            ansiedade: 0,
            exaustao_mental: 0,
            alto_para_raiva: 0,
            alto_para_tristeza: 0,
            voce_esta_bem: 0,
            inconclusivo:10,
        }},
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
    
    ##############################################################################################
    # Q4
    ##############################################################################################
    {"question": q4["q"], "options": [
        {"text": q4["a1"], "traits": {
            ansiedade: 1,
            exaustao_mental: 1
        }},
        {"text": q4["a2"], "traits": {
            exaustao_mental: 1,
            alto_para_raiva: 1
        }},
        {"text": q4["a3"], "traits": {
            alto_para_raiva: 1,
            alto_para_tristeza: 1
        }},
        {"text": q4["a4"], "traits": {
            alto_para_tristeza: 1,
            voce_esta_bem : 1
        }},
        {"text": q4["a5"], "traits": {
          inconclusivo: 1
        }}
    ]},
    ##############################################################################################
    # Q5
    ##############################################################################################
    {"question": q5["q"], "options": [
        {"text": q5["a1"], "traits": {
            ansiedade: 1,
            exaustao_mental: 1
        }},
        {"text": q5["a2"], "traits": {
            exaustao_mental: 1,
            alto_para_raiva: 1
        }},
        {"text": q5["a3"], "traits": {
            alto_para_raiva: 1,
            alto_para_tristeza: 1
        }},
        {"text": q5["a4"], "traits": {
            alto_para_tristeza: 1,
            voce_esta_bem : 1
        }},
        {"text": q5["a5"], "traits": {
          inconclusivo: 1
        }}
    ]},
   
    ##############################################################################################
    # Q8
    ##############################################################################################
    {"question": q8["q"], "options": [
        {"text": q8["a1"], "traits": {
            ansiedade: 1,
            exaustao_mental: 1
        }},
        {"text": q8["a2"], "traits": {
            exaustao_mental: 1,
            alto_para_raiva: 1
        }},
        {"text": q8["a3"], "traits": {
            alto_para_raiva: 1,
            alto_para_tristeza: 1
        }},
        {"text": q8["a4"], "traits": {
            alto_para_tristeza: 1,
            voce_esta_bem : 1
        }},
        {"text": q8["a5"], "traits": {
          inconclusivo: 1
        }}
    ]},
    ##############################################################################################
    # Q9
    ##############################################################################################
    {"question": q9["q"], "options": [
        {"text": q9["a1"], "traits": {
            ansiedade: 1,
            exaustao_mental: 1
        }},
        {"text": q9["a2"], "traits": {
            exaustao_mental: 1,
            alto_para_raiva: 1
        }},
        {"text": q9["a3"], "traits": {
            alto_para_raiva: 1,
            alto_para_tristeza: 1
        }},
        {"text": q9["a4"], "traits": {
            alto_para_tristeza: 1,
            voce_esta_bem : 1
        }},
        {"text": q9["a5"], "traits": {
          inconclusivo: 1
        }}
    ]},
    ##############################################################################################
    # Q10
    ##############################################################################################
    {"question": q10["q"], "options": [
        {"text": q10["a1"], "traits": {
            ansiedade: 1,
            exaustao_mental: 1
        }},
        {"text": q10["a2"], "traits": {
            exaustao_mental: 1,
            alto_para_raiva: 1
        }},
        {"text": q10["a3"], "traits": {
            alto_para_raiva: 1,
            alto_para_tristeza: 1
        }},
        {"text": q10["a4"], "traits": {
            alto_para_tristeza: 1,
            voce_esta_bem : 1
        }},
         {"text": q10["a5"], "traits": {
          inconclusivo: 1
        }}
    ]},
    ##############################################################################################
    # Q11
    ##############################################################################################
    {"question": q11["q"], "options": [
        {"text": q11["a1"], "traits": {
            ansiedade: 1,
            exaustao_mental: 1
        }},
        {"text": q11["a2"], "traits": {
            exaustao_mental: 1,
            alto_para_raiva: 1
        }},
        {"text": q11["a3"], "traits": {
            alto_para_raiva: 1,
            alto_para_tristeza: 1
        }},
        {"text": q11["a4"], "traits": {
            alto_para_tristeza: 1,
            voce_esta_bem : 1
        }},
         {"text": q11["a5"], "traits": {
          inconclusivo: 1
        }}
    ]},
    ##############################################################################################
    # Q12
    ##############################################################################################
    {"question": q12["q"], "options": [
        {"text": q12["a1"], "traits": {
            ansiedade: 1,
            exaustao_mental: 1
        }},
        {"text": q12["a2"], "traits": {
            exaustao_mental: 1,
            alto_para_raiva: 1
        }},
        {"text": q12["a3"], "traits": {
            alto_para_raiva: 1,
            alto_para_tristeza: 1
        }},
        {"text": q12["a4"], "traits": {
            alto_para_tristeza: 1,
            voce_esta_bem : 1
        }},
         {"text": q12["a5"], "traits": {
          inconclusivo: 1
        }}
    ]}
]