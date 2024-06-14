class Automato(object):
    def __init__(self,estados,transicoes, inicial,finais):
        self.e = estados
        self.t = transicoes
        self.alfabeto = []
        self.atual = inicial
        self.finais = finais


    def mostraAutomato(self):
        print('estados: ',self.e)
        print('transicoes: ',self.t)


    def processaString(self,string):
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

    def questao2(self, texto):
        print (texto)
        match = False
        inicioCount = 0
        finalCount = 0
        inicio = 0
        final = 0
        for i in texto: #percorrendo a cadeia
            #print('lendo a letra', i)
            match = False
            for j in self.t: #para cada letra da cadeia, verifica se existe uma transição naquele estado
                #print('comparando a letra: ',i,' no estado:',self.atual,'com a transição: ',j,)
                if (i == j[1]) & (self.atual == j[0]): #verificando a existencia da transição
                    #print(self. atual, ' -> ',i,' -> ',j[2])
                    if (self.atual == 'q0') & (j[2] == 'q1'):
                        #print('entrou aqui')
                        inicio = inicioCount + 1
                    elif (self.atual == 'q11') & (j[2] == 'q12'):
                        final = finalCount - 1
                        print('casamento nas posições', inicio,' ', final)
                    self.atual = j[2]
                    #print('atual agora ', self.atual)
                    match = True
                    break
            if not match:
                #print('nao foi')
                self.atual = 'q0'

            inicioCount += 1
            finalCount += 1