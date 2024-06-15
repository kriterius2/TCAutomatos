from automato import Automato

'''
letra A (ab*c*)*
    estados = ['q0','q1','q2']
    transicoes = [
        ['q0','a','q1'],
        ['q1','a','q1'],
        ['q1','b','q2'],
        ['q2','a','q1'],
        ['q2','b','q2'],
        ['q2','c','q3'],
        ['q3','a','q1']
        ]

inicial = 'q0'
finais = ['q0','q1','q2','q3']        

letra B aaa(b|c)* |(b|c)*aaa

estados ['q0','q1','q2','q3','q4','q5','q6','q7']
transicoes = [
    ['q0','a','q1'],
    ['q0','b','q4'],
    ['q0','c','q4'],
    ['q1','a','q2'],
    ['q2','a','q3'],
    ['q3','b','q3'],
    ['q3','c','q3'],
    ['q4','b','q4'],
    ['q4','c','q4'],
    ['q4','a','q5'],
    ['q5','a','q6'],
    ['q6','a','q7'],
]

inicial = 'q0'
finais = ['q3','q7']


letra C a*b|ab*
estados = ['q0','q1','q2','q3','q4']
transicoes = [
    ['q0','a','q1'],
    ['q0','b','q3'],
    ['q1','a','q2'],
    ['q1','b','q3'],
    ['q2','a','q2'],
    ['q2','b','q4'],
    ['q3','b','q3']
    ]

inicial = 'q0'
finais = ['q1','q3','q4']

letra d  a*b* (a | ac*)
estados = ['q0','q1','q2','q3']
transicoes = [
    ['q0','a','q1'],
    ['q0','b','q2'],
    ['q1','a','q1'],
    ['q1','b','q2'],
    ['q1','c','q3'],
    ['q2','a','q3'],
    ['q2','b','q2'],
    ['q3','c','q3']

]
inicial = 'q0'
finais = ['q1','q3']


======questão 2

estados = ['q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11']
transicoes = [
    ['q0',' ','q1'],
    ['q1','c','q2'],
    ['q2','o','q3'],
    ['q3','m','q4'],
    ['q4','p','q5'],
    ['q5','u','q6'],
    ['q6','t','q7'],
    ['q7','a','q8'],
    ['q8','d','q9'],
    ['q9','o','q10'],
    ['q10','r','q11'],
    ['q11',' ','q12']
    ]
    inicial = 'q1'
    finais = ['q11']

    texto = 'O computador é uma máquina capaz de variados tipos de tratamento automático de
informações ou processamento de dados. Entende-se por computador um sistema físico que
realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são
ícones da era da informação. O primeiro computador eletromecânico foi construído por
Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado
computador pessoal ou ainda computador doméstico.'




'''
estados = ['q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11']
transicoes = [
    ['q0',' ','q1'],
    ['q1','c','q2'],
    ['q1',' ','q1'],
    ['q2','o','q3'],
    ['q2',' ','q1'],
    ['q3','m','q4'],
    ['q3',' ','q1'],
    ['q4','p','q5'],
    ['q4',' ','q1'],
    ['q5','u','q6'],
    ['q5',' ','q1'],
    ['q6','t','q7'],
    ['q6',' ','q1'],
    ['q7','a','q8'],
    ['q7',' ','q1'],
    ['q8','d','q9'],
    ['q8',' ','q1'],
    ['q9','o','q10'],
    ['q9',' ','q1'],
    ['q10','r','q11'],
    ['q10',' ','q1'],
    ['q11',' ','q12'],
    ['q11','.','q12'],
    ['q11',':','q12'],
    ['q11',',','q12']
    ]
inicial = 'q1'
finais = ['q11']

texto = "O computador é uma máquina capaz de variados tipos de tratamento automático de informações ou processamento de dados. Entende-se por computador um sistema físico que realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são ícones da era da informação. O primeiro computador eletromecânico foi construído por Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado computador pessoal ou ainda computador doméstico." 
#texto = 'o computador é uma maquina com computador '
aut = Automato(estados,transicoes,inicial,finais)

#aut.mostraAutomato()

aut.questao2(texto)