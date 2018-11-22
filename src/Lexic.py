from Token import *

class Lexic:
    def __init__(self, states, reserved):
        self.states = states
        self.TS = []
        self.token_in = []
        self.reserved = reserved
        self.error = False
        self.readFonte()
        self.recognize()

    def getTS(self):
        return self.TS

    def getError(self):
        for t in self.TS:
            if t.erro == True:
                self.error = True
                return self.error

    #Reads the source code
    def readFonte(self):
        arquivo = open('../testcases/fonte.txt', 'r')
        lines = arquivo.read().splitlines()
        lines = list(filter(lambda a: a != '', lines))
        for token in lines:
            i = token.strip().split(' ')
            self.token_in.append(i)

    def printErrors(self):
        for t in self.TS:
            if t.erro == True:
                print('Erro léxico linha: ' + str(t.linha) + '  "'+ str(t.rotulo) + '"' )


    def recognize(self):
        current = 'S'
        idPointer = []
        pointer = None

        for l, line in enumerate(self.token_in):
            for token in line:
                for i in token:
                    if i in self.states[current].keys():
                        current = self.states[current][i][0]
                    else:
                        if len(token) == 1 and i in self.states[current].keys():
                                current = self.states[current][i][0]
                        else :
                            current = 'err'
                            break
                if current != 'err' and 'ε' in self.states[current].keys():
                    if token in self.reserved:
                        id = token
                    else:
                        id = 'Id'
                        if token not in idPointer:
                            idPointer.append(token)

                        pointer = idPointer.index(token)
                    novo = Token(token, l+1, id, current, False, pointer)
                    self.TS.append(novo)
                    pointer = None

                else:
                    error = False
                    id = "Id"
                    try:
                        float(token)
                        id = 'digit'
                    except:
                        error = True
                    novo = Token(token,l+1, id, 'err', error, pointer)
                    self.TS.append(novo)
                current = 'S'
        final = Token('EOF', l+1, 'EOF', current, False, None)
        self.TS.append(final)
