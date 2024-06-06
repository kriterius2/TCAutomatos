string = 'testando a string'
from automato import Automato

'''
letra A (ab*c*)*
    estados = ['q0','q1','q2']
    transicoes = [
        ['q0','a','q1'],
        ['q1','a','q1'],
        ['q1','b','q1'],
        ['q1','c','q2'],
        ['q2','c','q2'],
        ['q2','a','q1']
        ]

inicial = 'q0'
finais = ['q1','q2']        

letra B aaa(b|c)* |(b|c)*aaa

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

'''
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
aut = Automato(estados,transicoes,inicial,finais)

#aut.mostraAutomato()

aut.processaString('aba')