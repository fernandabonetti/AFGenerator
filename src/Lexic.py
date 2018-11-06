from Token import *

class Lexic:
    def __init__(self, states):
        self.states = states
        self.TS = []
        self.token_in = []
        self.readFonte()
        self.recognize()


    #Reads the source code
    def readFonte(self):
        arquivo = open('../testcases/fonte.txt', 'r')
        lines = arquivo.read().splitlines()
        lines = list(filter(lambda a: a != '', lines))
        for token in lines:
            i = token.strip().split(' ')
            self.token_in.append(i)

    def recognize(self):
        current = 'S'
        for l,line in enumerate(self.token_in):
            for token in line:
                #print(token, type(token))
                for i in token:
                    if i in self.states[current].keys():
                        current = self.states[current][i][0]
                    else:
                        current = 'err'
                        break
                if current != 'err' and 'ε' in self.states[current].keys():
                    novo = Token(token, l+1, 'id', current, False)
                    self.TS.append(novo)

                else:
                    error = False
                    id = "id"
                    try:
                        float(token)
                        id = 'num'
                    except:
                        error = True
                    novo = Token(token,l+1, id , 'err', error)
                    self.TS.append(novo)

                current = 'S'
        for t in self.TS:
            if t.erro == True:
                print('erro léxico linha: ' + str(t.linha) + '  "'+ str(t.rotulo) + '"' )
            t.printToken()
