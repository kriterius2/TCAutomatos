class Automato(object):
    def __init__(self,estados,transicoes, inicial,finais):
        self.e = estados
        self.t = transicoes
        self.alfabeto = []
        self.inicial = inicial
        self.atual = inicial
        self.finais = finais


    def mostraAutomato(self):
        print('estados: ',self.e)
        print('transicoes: ',self.t)


    def processaString(self,string):
        self.atual = self.inicial
        match = False
        print("processando a cadeia: ", string)
        for i in string: #percorrendo a cadeia
            match = False
            for j in self.t: #para cada letra da cadeia, verifica se existe uma transição naquele estado
                if (i == j[1]) & (self.atual == j[0]): #verificando a existencia da transição
                    print(self. atual, ' -> ',i,' -> ',j[2])
                    self.atual = j[2]
                    match = True
                    break
            if not match: #caso nao tenha encontrado nenhuma transição  a cadeia é recusada
                print('PALAVRA RECUSADA')
                return

        if self.atual in self.finais: #apos percorrer a cadeia, caso o automato esteja em um estado final, a palavra é recusada
            print('PALAVRA ACEITA')
        else:
            print('PALAVRA RECUSADA')  
    

    def ocorrencias(self, texto):
        print('===========================================================================================')
        print (texto)
        print('===========================================================================================')
        match = False
        inicioCount = 0
        finalCount = 0
        inicio = 0
        final = 0
        for i in texto: #percorrendo a cadeia
            match = False
            for j in self.t: #para cada letra da cadeia, verifica se existe uma transição naquele estado
                if (i == j[1]) & (self.atual == j[0]): #verificando a existencia da transição
                    if (j[2] == 'q1'):
                        inicio = inicioCount + 1
                    elif (self.atual == 'q11') & (j[2] == 'q12'):
                        final = finalCount - 1
                        print('casamento nas posições', inicio,'a', final)
                        inicio = inicioCount + 1
                    self.atual = j[2]
                    match = True
                    break
            if not match:
                self.atual = 'q0'

            inicioCount += 1
            finalCount += 1